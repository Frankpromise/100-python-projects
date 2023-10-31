import os
from shutil import move


def sort_files(directory_path):
    # sort files in  directory by their extension
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        # sort if it's a file
        if os.path.isfile(file_path):
            file_extension = filename.split('.')[-1]
            destination_directory = os.path.join(
                directory_path, file_extension)
            #  if not present
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            # move the file into its extension directory
            move(file_path, os.path.join(destination_directory, filename))

# sort_files("test/")
