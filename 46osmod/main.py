import os

print(dir(os))

for i in range(0,100):
    os.mkdir(f'osmod/Day {i+1}')

#rename    
for i in range(0, 100):
    os.rename(f"data/Tutorial{i+1}", f"data/Tutorial {i+1}")

#to list contain
folders = os.listdir("osmod")
for folder in folders:
    print(folder)
    print(os.listdir(f'osmod/{folder}'))
    


import os
# Base directory where the folders will be created
base_dir = "osmod"

for i in range(1, 11):
    # Create folder name
    folder_name = f"day{i}"
    
    # Create the full path for the folder
    folder_path = os.path.join(base_dir, folder_name)
    
    # Create the folder
    os.makedirs(folder_path, exist_ok=True)
    
    # Create a text file in the folder
    file_path = os.path.join(folder_path, "file.txt")
    with open(file_path, "w") as file:
        file.write(f"This is the text file for {folder_name}")

print("Folders and files created successfully.")

#to delete
import shutil
import os

# Base directory where the folders are located
base_dir = "osmod"

for i in range(1, 11):
    # Create folder name
    folder_name = f"day{i}"
    
    # Create the full path for the folder
    folder_path = os.path.join(base_dir, folder_name)
    
    # Check if the folder exists and delete it
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)

print("Folders and files deleted successfully.")
