import os
import yaml

# Path to the folder containing the files for the sidebar
folder_path = './pages/Testpurpose'  # Update this with your folder path

# Path to the YAML file where the sidebar content will be written
sidebar_file_path = './_data/sidebars/mydoc_sidebar.yml'  # Update this with your desired sidebar file path

def generate_sidebar():
    # Fetch the list of files in the folder
    files = os.listdir(folder_path)

    # Filter out directories, if any
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

    # Convert the list of files to a dictionary suitable for YAML
    sidebar_content = [{'title': file, 'url': file} for file in files]

    # Write the sidebar content to the YAML file
    with open(sidebar_file_path, 'w') as sidebar_file:
        yaml.dump(sidebar_content, sidebar_file, default_flow_style=False)

    print(f"Sidebar content generated and saved to '{sidebar_file_path}'")

if __name__ == "__main__":
    generate_sidebar()
