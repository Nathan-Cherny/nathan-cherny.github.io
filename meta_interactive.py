import os
import json
from bs4 import BeautifulSoup

# Base directory containing your static HTML files
DIRECTORY = "."
EXTENSION = ".html"

def prompt_for_field(label, current_value):
    """Displays the current value and prompts the user for a new one.
    Returns the new input, or the current value if the user presses ENTER."""
    print(f"\n--- {label} ---")
    print(f"Current: {current_value if current_value else '[EMPTY]'}")
    user_input = input("New Value (Press ENTER to keep current): ").strip()
    return user_input if user_input else current_value

def process_html_file(filepath):
    """Reads an HTML file, interactively prompts for metadata, and saves changes."""
    print("\n" + "=" * 80)
    print(f" EDITING FILE: {filepath}")
    print("=" * 80)

    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # -------------------------------------------------------------------------
    # 1. PAGE TITLE (<title>)
    # -------------------------------------------------------------------------
    title_tag = soup.find("title")
    current_title = title_tag.string.strip() if (title_tag and title_tag.string) else ""
    new_title = prompt_for_field("Page Title (<title>)", current_title)
    if title_tag:
        title_tag.string = new_title

    # -------------------------------------------------------------------------
    # 2. META DESCRIPTION (<meta name="description">)
    # -------------------------------------------------------------------------
    meta_desc = soup.find("meta", attrs={"name": "description"})
    current_desc = meta_desc["content"].strip() if (meta_desc and meta_desc.get("content")) else ""
    new_desc = prompt_for_field("Meta Description (Search Engines)", current_desc)
    if meta_desc:
        meta_desc["content"] = new_desc

    # -------------------------------------------------------------------------
    # 3. OPEN GRAPH TITLE (<meta property="og:title">)
    # -------------------------------------------------------------------------
    og_title = soup.find("meta", property="og:title")
    current_og_title = og_title["content"].strip() if (og_title and og_title.get("content")) else new_title
    new_og_title = prompt_for_field("Open Graph Title (og:title)", current_og_title)
    if og_title:
        og_title["content"] = new_og_title

    # -------------------------------------------------------------------------
    # 4. OPEN GRAPH DESCRIPTION (<meta property="og:description">)
    # -------------------------------------------------------------------------
    og_desc = soup.find("meta", property="og:description")
    current_og_desc = og_desc["content"].strip() if (og_desc and og_desc.get("content")) else new_desc
    new_og_desc = prompt_for_field("Open Graph Description (og:description)", current_og_desc)
    if og_desc:
        og_desc["content"] = new_og_desc

    # -------------------------------------------------------------------------
    # 5. OPEN GRAPH IMAGE (<meta property="og:image">)
    # -------------------------------------------------------------------------
    og_img = soup.find("meta", property="og:image")
    current_og_img = og_img["content"].strip() if (og_img and og_img.get("content")) else ""
    new_og_img = prompt_for_field("Open Graph / Feature Image Path (og:image)", current_og_img)
    if og_img:
        og_img["content"] = new_og_img

    # -------------------------------------------------------------------------
    # 6. JSON-LD SCHEMA GRAPH (YOAST SYNCHRONIZATION)
    # -------------------------------------------------------------------------
    schema_script = soup.find("script", type="application/ld+json", class_="yoast-schema-graph")
    if schema_script and schema_script.string:
        try:
            schema_data = json.loads(schema_script.string)
            if "@graph" in schema_data:
                for item in schema_data["@graph"]:
                    # Update WebPage metadata
                    if item.get("@type") == "WebPage":
                        item["name"] = new_title
                        item["description"] = new_desc
                        if new_og_img:
                            item["thumbnailUrl"] = new_og_img
                    
                    # Update ImageObject if primary image reference exists
                    elif item.get("@type") == "ImageObject" and item.get("@id", "").endswith("#primaryimage"):
                        if new_og_img:
                            item["url"] = new_og_img
                            item["contentUrl"] = new_og_img

            schema_script.string = json.dumps(schema_data, indent=2)
        except Exception as e:
            print(f"[Warning] Could not parse/update JSON-LD Schema: {e}")

    # Write changes back to the HTML file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(str(soup))

    print(f"\n[✓] Successfully updated: {filepath}\n")

def main():
    file_paths = []
    
    # Collect all HTML files
    for root, _, files in os.walk(DIRECTORY):
        for file in files:
            if file.endswith(EXTENSION):
                file_paths.append(os.path.join(root, file))

    total_files = len(file_paths)
    print(f"Found {total_files} HTML file(s) to review.")

    for idx, filepath in enumerate(file_paths, start=1):
        print(f"\nProgress: File {idx} of {total_files}")
        process_html_file(filepath)

    print("\n" + "=" * 80)
    print(" ALL FILES HAVE BEEN PROCESSED AND UPDATED!")
    print("=" * 80)

if __name__ == "__main__":
    main()