import os
import yaml

# Path to the folder containing the files for the sidebar
folder_path = './pages/Testpurpose'  # Update this with your folder path

# Path to the YAML file where the sidebar content will be written
sidebar_file_path = './_data/sidebars/mydoc_sidebar.yml'  # Update this with your desired sidebar file path

import os
files = [f for f in os.listdir('folder_path') if os.path.isfile(f)]

sidebar_file = open('sidebar_file_path', 'w')

for file in files:
	if ".md" in file:
		name = file.split(".md")
		file = file.replace(" ", "%20")
		sidebar_file.write( f"* [{name[0]}]({file})\n" )

sidebar_file.close()
