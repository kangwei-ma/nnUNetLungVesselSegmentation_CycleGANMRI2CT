import os
import shutil

def move_files(src_root, dest_folder, folder_name):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    for root, dirs, files in os.walk(src_root):
        if os.path.basename(root) == folder_name:
            for file in files:
                src_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_folder, file)
                shutil.move(src_file_path, dest_file_path)

# source folder and destination folder
src_directory = r'C:\Users\lyubi\OneDrive - University of Canberra\Desktop\2023Intern\parse2022-dataset\train\train_original'
#images_dest_folder = r'C:\Users\lyubi\OneDrive - University of Canberra\Desktop\2023Intern\parse2022-dataset\train\imagesTr'
labels_dest_folder = r'C:\Users\lyubi\OneDrive - University of Canberra\Desktop\2023Intern\parse2022-dataset\train\labelsTr_without0000'

# moving files from image folders
#move_files(src_directory, images_dest_folder, 'image')

# moving files from label folders
move_files(src_directory, labels_dest_folder, 'label')
