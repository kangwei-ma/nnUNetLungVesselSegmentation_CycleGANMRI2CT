import os

def rename_files_with_suffix(root_folder, suffix="_0000"):
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            # checking whether there's double extension name .nii.gz
            if file.endswith(".nii.gz"):
                # seperating file name and extension name
                file_name = file[:-7]  # remove the .nii.gz，to get the file name
                new_file_name = file_name + suffix + ".nii.gz"
            else:
                # for non nii.gz files, actually not used since we only have nii.gz files
                file_name, file_extension = os.path.splitext(file)
                new_file_name = file_name + suffix + file_extension

            # construct the path for old file and new file
            old_file_path = os.path.join(root, file)
            new_file_path = os.path.join(root, new_file_name)

            # rename the files
            os.rename(old_file_path, new_file_path)

# call the function defined above，'your_directory_path' replaced by my filepath
rename_files_with_suffix(r"C:\Users\lyubi\OneDrive - University of Canberra\Desktop\2023Intern\parse2022-dataset\train\train_renaming_trial2")
