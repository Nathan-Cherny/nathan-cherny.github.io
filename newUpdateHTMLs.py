#!/usr/bin/env python3
"""
updateHTMLs.py

Toolkit for maintaining a static HTML site: bulk header/footer/head template
updates, interactive per-page metadata editing, per-page "last modified"
metadata syncing (from real git commit history), and sitemap.xml generation.

USAGE (run from your repo root, or set DIRECTORY/REPO_DIR below):
    python3 updateHTMLs.py template     # apply new header/footer/head across all pages
    python3 updateHTMLs.py meta         # interactively edit title/description/OG tags per page
    python3 updateHTMLs.py lastmod      # sync each page's <meta modified> + JSON-LD dateModified to git history
    python3 updateHTMLs.py sitemap      # regenerate sitemap.xml from git history
    python3 updateHTMLs.py all          # lastmod, then sitemap (safe to run after any content edit)

Requires: beautifulsoup4  (pip install beautifulsoup4)
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from xml.sax.saxutils import escape

from bs4 import BeautifulSoup

# =============================================================================
# CONFIG — edit these to match your project
# =============================================================================

DIRECTORY = "."                     # root folder to walk for .html files
EXTENSION = ".html"
REPO_DIR = Path(__file__).parent    # root of your git repo (for git log lookups)
BASE_URL = "https://xsotec.com"     # your site's domain, no trailing slash

EXCLUDE_DIRS = {".git", "node_modules", "_site", "dist", "build"}
EXCLUDE_FILES = {"404.html"}        # never indexed / never sitemap'd

SITEMAP_OUTPUT_FILE = REPO_DIR / "sitemap.xml"


# =============================================================================
# SHARED HELPERS
# =============================================================================

def collect_html_files(base_dir: str = DIRECTORY) -> list[Path]:
    """Return all .html files under base_dir, skipping excluded dirs/files."""
    files = []
    for root, dirs, filenames in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for name in filenames:
            if name.endswith(EXTENSION) and name not in EXCLUDE_FILES:
                files.append(Path(root) / name)
    return sorted(files)


def file_to_url_path(filepath: Path, base_dir: str = DIRECTORY) -> str:
    """Map a file path to its site URL path, e.g. ./about/index.html -> /about/"""
    dir_path = os.path.dirname(filepath) or "."  # empty string means "current dir"
    rel_dir = os.path.relpath(dir_path, base_dir).replace("\\", "/")
    return "/" if rel_dir == "." else f"/{rel_dir}/"


def get_last_commit_date(filepath: Path) -> str | None:
    """Return the ISO 8601 commit date (%cI) of the last commit touching this
    file, or None if it has no git history (e.g. new/uncommitted file)."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cI", "--", str(filepath)],
            cwd=REPO_DIR,
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"  git error for {filepath}: {e.stderr.strip()}", file=sys.stderr)
        return None
    return result.stdout.strip() or None


# =============================================================================
# 1. BULK TEMPLATE UPDATES (header / footer / head)
# =============================================================================
# Pass in the new header/footer/head as strings. Each is only applied if you
# provide it, so you can update just one piece (e.g. only the footer) without
# touching the others. This preserves the original split-based logic, just
# wrapped in functions instead of running as loose top-level code.

HEADER_START = '<header id="site-header" class="header-footer-group">'
HEAD_START = "<head>"
HEAD_END = "</head>"
FOOTER_START = "</main>"
FOOTER_END = '<script type="speculationrules">'

OLD_BREADCRUMB_BLOCK = """{
    "@type": "BreadcrumbList",
    "@id": "/#breadcrumb",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "name": "Home" }
    ]
  }"""


def _build_breadcrumb_json(url_path: str) -> str:
    """Generate the Yoast-style breadcrumb JSON-LD block for a given URL path."""
    if url_path == "/":
        return """{
    "@type": "BreadcrumbList",
    "@id": "/#breadcrumb",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "name": "Home", "item": "%s/" }
    ]
  }""" % BASE_URL

    parts = [p for p in url_path.split("/") if p]
    items = [
        '{ "@type": "ListItem", "position": 1, "name": "Home", "item": "%s/" }' % BASE_URL
    ]
    current_path = ""
    for i, part in enumerate(parts):
        current_path += f"/{part}"
        page_name = part.replace("-", " ").title()
        items.append(
            f'{{ "@type": "ListItem", "position": {i + 2}, "name": "{page_name}", '
            f'"item": "{BASE_URL}{current_path}/" }}'
        )
    items_str = ",\n              ".join(items)
    return f"""{{
    "@type": "BreadcrumbList",
    "@id": "{url_path}#breadcrumb",
    "itemListElement": [
      {items_str}
    ]
  }}"""


def _apply_head_update(html: str, url_path: str, new_head: str) -> str:
    if HEAD_START not in html or HEAD_END not in html:
        return html
    old_head = HEAD_START + html.split(HEAD_END)[0].split(HEAD_START)[1]

    custom_head = new_head
    custom_head = custom_head.replace(
        '<link rel="canonical" href="/" />', f'<link rel="canonical" href="{url_path}" />'
    )
    custom_head = custom_head.replace(
        '<meta property="og:url" content="/" />', f'<meta property="og:url" content="{url_path}" />'
    )
    custom_head = custom_head.replace('"@id": "/"', f'"@id": "{url_path}"')
    custom_head = custom_head.replace('"url": "/"', f'"url": "{url_path}"')
    custom_head = custom_head.replace('"/#website"', f'"{url_path}#website"')
    custom_head = custom_head.replace(OLD_BREADCRUMB_BLOCK, _build_breadcrumb_json(url_path))

    return html.replace(old_head, custom_head)


def _apply_header_update(html: str, new_header: str) -> str:
    if HEADER_START not in html:
        return html
    # header runs from HEADER_START to the start of <main id="site-content">
    main_marker = '<main id="site-content">'
    if main_marker not in html:
        return html
    old_header = HEADER_START + html.split(main_marker)[0].split(HEADER_START)[1]
    return html.replace(old_header, new_header)


def _apply_footer_update(html: str, new_footer: str) -> str:
    if FOOTER_START not in html or FOOTER_END not in html:
        return html
    old_footer = FOOTER_START + html.split(FOOTER_START)[1].split(FOOTER_END)[0]
    return html.replace(old_footer, new_footer)


def update_templates(new_header: str | None = None,
                      new_footer: str | None = None,
                      new_head: str | None = None,
                      base_dir: str = DIRECTORY) -> None:
    """Apply new header/footer/head templates across every HTML file.
    Only the pieces you pass in are touched; pass None to skip a piece."""
    files = collect_html_files(base_dir)
    print(f"Applying template updates to {len(files)} file(s)...")

    for filepath in files:
        url_path = file_to_url_path(filepath, base_dir)
        html = filepath.read_text(encoding="utf-8")

        if new_header:
            html = _apply_header_update(html, new_header)
        if new_head:
            html = _apply_head_update(html, url_path, new_head)
        if new_footer:
            html = _apply_footer_update(html, new_footer)

        filepath.write_text(html, encoding="utf-8")

    print("Template update complete.")


# =============================================================================
# 2. INTERACTIVE PER-PAGE METADATA EDITOR
# =============================================================================

def _prompt_for_field(label: str, current_value: str) -> str:
    print(f"\n--- {label} ---")
    print(f"Current: {current_value if current_value else '[EMPTY]'}")
    user_input = input("New Value (Press ENTER to keep current): ").strip()
    return user_input if user_input else current_value


def _sync_json_ld_schema(soup: BeautifulSoup, new_title: str, new_desc: str, new_og_img: str) -> None:
    """Keep the Yoast-style JSON-LD @graph in sync with title/description/image."""
    schema_script = soup.find("script", type="application/ld+json", class_="yoast-schema-graph")
    if not (schema_script and schema_script.string):
        return
    try:
        schema_data = json.loads(schema_script.string)
        for item in schema_data.get("@graph", []):
            if item.get("@type") == "WebPage":
                item["name"] = new_title
                item["description"] = new_desc
                if new_og_img:
                    item["thumbnailUrl"] = new_og_img
            elif item.get("@type") == "ImageObject" and item.get("@id", "").endswith("#primaryimage"):
                if new_og_img:
                    item["url"] = new_og_img
                    item["contentUrl"] = new_og_img
        schema_script.string = json.dumps(schema_data, indent=2)
    except Exception as e:
        print(f"[Warning] Could not parse/update JSON-LD Schema: {e}")


def process_html_file(filepath: Path) -> None:
    """Interactively prompt for and update a single page's metadata."""
    print("\n" + "=" * 80)
    print(f" EDITING FILE: {filepath}")
    print("=" * 80)

    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    title_tag = soup.find("title")
    current_title = title_tag.string.strip() if (title_tag and title_tag.string) else ""
    new_title = _prompt_for_field("Page Title (<title>)", current_title)
    if title_tag:
        title_tag.string = new_title

    meta_desc = soup.find("meta", attrs={"name": "description"})
    current_desc = meta_desc["content"].strip() if (meta_desc and meta_desc.get("content")) else ""
    new_desc = _prompt_for_field("Meta Description (Search Engines)", current_desc)
    if meta_desc:
        meta_desc["content"] = new_desc

    og_title = soup.find("meta", property="og:title")
    current_og_title = og_title["content"].strip() if (og_title and og_title.get("content")) else new_title
    new_og_title = _prompt_for_field("Open Graph Title (og:title)", current_og_title)
    if og_title:
        og_title["content"] = new_og_title

    og_desc = soup.find("meta", property="og:description")
    current_og_desc = og_desc["content"].strip() if (og_desc and og_desc.get("content")) else new_desc
    new_og_desc = _prompt_for_field("Open Graph Description (og:description)", current_og_desc)
    if og_desc:
        og_desc["content"] = new_og_desc

    og_img = soup.find("meta", property="og:image")
    current_og_img = og_img["content"].strip() if (og_img and og_img.get("content")) else ""
    new_og_img = _prompt_for_field("Open Graph / Feature Image Path (og:image)", current_og_img)
    if og_img:
        og_img["content"] = new_og_img

    _sync_json_ld_schema(soup, new_title, new_desc, new_og_img)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(soup.prettify())

    print(f"\n[OK] Successfully updated: {filepath}\n")


def run_meta_interactive(base_dir: str = DIRECTORY) -> None:
    files = collect_html_files(base_dir)
    total = len(files)
    print(f"Found {total} HTML file(s) to review.")

    for idx, filepath in enumerate(files, start=1):
        print(f"\nProgress: File {idx} of {total}")
        process_html_file(filepath)

    print("\n" + "=" * 80)
    print(" ALL FILES HAVE BEEN PROCESSED AND UPDATED!")
    print("=" * 80)


# =============================================================================
# 3. NEW: SYNC "LAST MODIFIED" METADATA FROM GIT HISTORY
# =============================================================================
# Updates two things per page, sourced from the real git commit date so the
# value can never drift into "fake" territory the way a hardcoded date would:
#   - <meta property="article:modified_time" content="...">  (created if missing)
#   - JSON-LD "dateModified" field in the Yoast schema graph, if present

def _update_modified_meta_tag(soup: BeautifulSoup, iso_date: str) -> None:
    tag = soup.find("meta", property="article:modified_time")
    if tag:
        tag["content"] = iso_date
    else:
        tag = soup.new_tag("meta", property="article:modified_time", content=iso_date)
        if soup.head:
            soup.head.append(tag)


def _update_json_ld_date_modified(soup: BeautifulSoup, iso_date: str) -> None:
    schema_script = soup.find("script", type="application/ld+json", class_="yoast-schema-graph")
    if not (schema_script and schema_script.string):
        return
    try:
        schema_data = json.loads(schema_script.string)
        for item in schema_data.get("@graph", []):
            if item.get("@type") == "WebPage":
                item["dateModified"] = iso_date
        schema_script.string = json.dumps(schema_data, indent=2)
    except Exception as e:
        print(f"[Warning] Could not update JSON-LD dateModified: {e}")


def update_lastmod_metadata(base_dir: str = DIRECTORY) -> None:
    """Sync each page's in-HTML 'last modified' metadata to its real git
    commit date. Skips files with no git history (nothing to sync yet)."""
    files = collect_html_files(base_dir)
    print(f"Syncing lastmod metadata for {len(files)} file(s)...")

    updated, skipped = 0, 0
    for filepath in files:
        iso_date = get_last_commit_date(filepath)
        if iso_date is None:
            print(f"  SKIP (no git history): {filepath}")
            skipped += 1
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")

        _update_modified_meta_tag(soup, iso_date)
        _update_json_ld_date_modified(soup, iso_date)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(soup.prettify())
        updated += 1

    print(f"Lastmod sync complete: {updated} updated, {skipped} skipped.")


# =============================================================================
# 4. SITEMAP GENERATION
# =============================================================================

def build_sitemap_entries(base_dir: str = DIRECTORY) -> list[dict]:
    entries = []
    for filepath in collect_html_files(base_dir):
        url_path = file_to_url_path(filepath, base_dir)
        lastmod = get_last_commit_date(filepath)
        if lastmod is None:
            print(f"  WARNING: no git history for {filepath}, omitting lastmod")
        entries.append({"loc": BASE_URL + url_path, "lastmod": lastmod})
    return entries


def write_sitemap(entries: list[dict], output_file: Path = SITEMAP_OUTPUT_FILE) -> None:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for entry in entries:
        lines.append("  <url>")
        lines.append(f"    <loc>{escape(entry['loc'])}</loc>")
        if entry["lastmod"]:
            lines.append(f"    <lastmod>{entry['lastmod']}</lastmod>")
        lines.append("  </url>")
    lines.append("</urlset>")

    output_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(entries)} URLs to {output_file}")


def make_sitemap(base_dir: str = DIRECTORY) -> None:
    print(f"Scanning {base_dir} for HTML files...")
    entries = build_sitemap_entries(base_dir)
    if not entries:
        print("No HTML files found. Check DIRECTORY config.", file=sys.stderr)
        sys.exit(1)
    write_sitemap(entries)


# =============================================================================
# CLI
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="Static site HTML maintenance toolkit")
    parser.add_argument(
        "command",
        choices=["template", "meta", "lastmod", "sitemap", "all"],
        help=(
            "template: apply header/footer/head changes (edit the "
            "new_header/new_footer/new_head variables in __main__ first) | "
            "meta: interactively edit per-page title/description/OG tags | "
            "lastmod: sync each page's modified-time metadata to git history | "
            "sitemap: regenerate sitemap.xml from git history | "
            "all: lastmod + sitemap (recommended after any content edit)"
        ),
    )
    args = parser.parse_args()

    if args.command == "template":
        # Fill these in with your actual template strings before running,
        # or call update_templates(...) directly from your own script.
        new_header = None
        new_footer = None
        new_head = None
        if not any([new_header, new_footer, new_head]):
            print("No new_header/new_footer/new_head set — edit __main__ in this "
                  "file (or call update_templates() directly) before running "
                  "'template'.", file=sys.stderr)
            sys.exit(1)
        update_templates(new_header=new_header, new_footer=new_footer, new_head=new_head)

    elif args.command == "meta":
        run_meta_interactive()

    elif args.command == "lastmod":
        update_lastmod_metadata()

    elif args.command == "sitemap":
        make_sitemap()

    elif args.command == "all":
        update_lastmod_metadata()
        make_sitemap()


if __name__ == "__main__":
    main()