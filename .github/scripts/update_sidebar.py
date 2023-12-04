import os
import json

folder_path = "./pages/mydoc"
sidebar_path = "./sidebars/home_sidebar.yml"

# Get a list of files in the folder
files = os.listdir(folder_path)

# Update the sidebar configuration
with open(sidebar_path, 'r') as f:
    sidebar = json.load(f)

# Modify the sidebar based on the new files
for file in files:
    sidebar["sections"]["New Files"].append({"text": file, "url": f"/path/to/folder/{file}"})

# Save the updated sidebar
with open(sidebar_path, 'w') as f:
    json.dump(sidebar, f, indent=2)
