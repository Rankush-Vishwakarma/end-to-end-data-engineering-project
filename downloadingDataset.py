import kagglehub
import shutil
import os

# Download into kagglehub cache
path = kagglehub.dataset_download("ukveteran/adventure-works", force_download=True)

print("Dataset cache path:", path)

# Copy everything from cache to current folder
current_dir = os.getcwd()
for item in os.listdir(path):
    s = os.path.join(path, item)
    d = os.path.join(current_dir, item)
    if os.path.isdir(s):
        shutil.copytree(s, d, dirs_exist_ok=True)
    else:
        shutil.copy2(s, d)

print("Files copied to:", current_dir)
