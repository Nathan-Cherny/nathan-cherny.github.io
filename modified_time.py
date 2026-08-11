import os
import json
from datetime import datetime, timezone
from bs4 import BeautifulSoup

# Base directory containing your HTML files
DIRECTORY = "."
EXTENSION = ".html"

def update_modified_times(directory=".", extension=".html"):
    # Generate the current UTC timestamp in ISO 8601 format (e.g., "2026-08-11T13:43:41+00:00")
    current_iso_time = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
    
    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_paths.append(os.path.join(root, file))

    print(f"Updating modified timestamp to '{current_iso_time}' across {len(file_paths)} file(s)...\n")

    updated_count = 0

    for filepath in file_paths:
        with open(filepath, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")

        file_changed = False

        # 1. Update <meta property="article:modified_time" content="..." />
        meta_modified = soup.find("meta", property="article:modified_time")
        if meta_modified:
            meta_modified["content"] = current_iso_time
            file_changed = True

        # 2. Update JSON-LD Schema "dateModified"
        schema_script = soup.find("script", type="application/ld+json", class_="yoast-schema-graph")
        if schema_script and schema_script.string:
            try:
                schema_data = json.loads(schema_script.string)
                if "@graph" in schema_data:
                    for item in schema_data["@graph"]:
                        # Update dateModified wherever it exists in the schema graph
                        if "dateModified" in item:
                            item["dateModified"] = current_iso_time
                            file_changed = True

                schema_script.string = json.dumps(schema_data, indent=2)
            except Exception as e:
                print(f"[Warning] Could not parse JSON-LD in {filepath}: {e}")

        # Save back to file if changes were made
        if file_changed:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(str(soup))
            print(f"[✓] Updated timestamp in: {filepath}")
            updated_count += 1
        else:
            print(f"[-] No modified_time meta tags found in: {filepath}")

    print("\n" + "=" * 60)
    print(f" COMPLETE: Updated {updated_count} out of {len(file_paths)} files.")
    print("=" * 60)

if __name__ == "__main__":
    update_modified_times(DIRECTORY, EXTENSION)