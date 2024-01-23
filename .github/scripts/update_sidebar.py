import os
import shutil
import yaml

folder_path = "./pages/Testpurpose"
sidebar_path = "./_data/sidebars/mydoc_sidebar.yml"

# Get a list of files in the folder
files = os.listdir(folder_path)

# Update the sidebar configuration
with open(sidebar_path, 'r') as f:
    sidebar = yaml.safe_load(f)

a = sidebar['entries'][0]['folders'][0]['folderitems']
for file in files:
    z = {"title": file , "url": f"/{file}"}   #erstellen eines neuen dicts in der richtigen Formatierung

a.append(z) # eine neues dict wird damit hinzugefügt

with open(sidebar_path, 'w') as f:
    json.dump(sidebar, f, indent=2)





# 8
