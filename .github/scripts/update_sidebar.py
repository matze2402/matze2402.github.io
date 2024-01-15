import os
import yaml

folder_path = "./pages/mydoc"
sidebar_path = "./_data/sidebars/home_sidebar.yml"

# Get a list of files in the folder
files = os.listdir(folder_path)

# Update the sidebar configuration
with open(sidebar_path, 'r') as f:
    sidebar = yaml.safe_load(f)

# Modify the sidebar based on the new files
for file in files:
   sidebar['entries'][0]['folders'][0]['folderitems'].append({"title": file , "url": f"./pages/mydoc/{file}"})

# Save the updated sidebar
with open(sidebar_path, 'w') as f:
    yaml.dump(sidebar, f, indent=2)
