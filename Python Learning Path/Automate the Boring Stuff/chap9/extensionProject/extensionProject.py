#! python3
# This program copy files wirth certain extension into a new folder

import os, shutil

# Ask user for file extension to copy files of the same kind and the destination folder name in wich files will be paste
print("Folder to copy files into: ")
new_folder_Name = input()
print("Extension to copy: ")
extension_Name = input()

# Creating the folder
current_directory = os.getcwd()  # Current folder
new_folder_Path = os.path.join(current_directory, new_folder_Name)
os.mkdir(new_folder_Path)


# Iterate through the folder tree looking for files with the choosed extension
old_files_path = "G:\\OneDrive\\Python Learning Path\\Automate the Boring Stuff\\chap9"

for root, dirs, files in os.walk(old_files_path):

     # If the loop go into new folder dont copy any files
     if root == os.path.join(current_directory, new_folder_Name):
          continue
     else:
          for file in files:
               if file.endswith(extension_Name) == True:
                    file_source = os.path.join(root, file)
                    file_destination = os.path.join(new_folder_Path)

                    shutil.copy(file_source, file_destination)
               
               

               


     

     # TODO After finding the file copy and paste it into the new folder 

