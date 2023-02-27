import os
import shutil

# Set the path of the main folder
main_folder = "D:\Artem\ijkn hbg\Bests"

# Initialize the counter for renaming
counter = 1

# Loop through all the subfolders
for root, dirs, files in os.walk(main_folder):
    if root == "Best 42" or root == "Best 43":
        for file in files:
            # Check if the file is a .jpg file
            if file.lower().endswith('.jpg'):
                # Set the path of the subfolder
                subfolder_path = os.path.join(root, file)
                # Set the new filename
                new_filename = str(counter) + '.jpg'
                # Set the path of the new file
                new_file_path = os.path.join(main_folder, new_filename)
                # Check if the new filename already exists in the main folder
                while os.path.exists(new_file_path):
                    # If the new filename already exists, increment the counter and generate a new filename
                    counter += 1
                    new_filename = str(counter) + '.jpg'
                    new_file_path = os.path.join(main_folder, new_filename)
                # Copy the file to the main folder and rename it
                shutil.copy(subfolder_path, new_file_path)
                # Increment the counter for renaming
                counter += 1