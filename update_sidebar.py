import os 
repo_path = os.getcwd()
files = [f for f in os.listdir(repo_path) if os.path.isfile(os.path.join(repo_path, f))]
print(files)
