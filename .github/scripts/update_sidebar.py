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
    z = {"title": file , "url": f"/{file}"}   

a.append(z) 

with open(sidebar_path, 'w') as f:
    yaml.dump(sidebar, f, indent=2)


def move_files(source_folder, destination_folder):
    # Check if the source folder exists
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
        return

    # Check if the destination folder exists, create it if not
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Get a list of all files in the source folder
    files = os.listdir(source_folder)

    # Move each file to the destination folder
    for file in files:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)
        shutil.move(source_path, destination_path)
        print(f"Moved: {file}")

# # Example usage:
source_folder  =  "C:/Users/smmagack/Desktop/documentation-theme-jekyll-gh-pages/pages/Testpurpose"
destination_folder = "C:/Users/smmagack/Desktop/documentation-theme-jekyll-gh-pages/pages/Testordner_neu"

move_files(source_folder, destination_folder)
    
    
    






