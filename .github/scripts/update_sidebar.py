import os
import json

folder_path = import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

sidebar_path = "matze2402/matze2402.github.io/blob/main/_data/sidebars/home_sidebar.yml"

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
