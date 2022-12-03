import os


def new_directory(directory, filename):
# check if directory already exist
    if os.path.isdir(directory) == False:
        os.mkdir(directory)


    # create the new file inside the directory
    os.chdir(directory)
    with open(filename, "w") as file:
        pass


    # lets return the list of files in directory
    return os.listdir(os.path.join(os.getcwd()))


print(new_directory("test_dir", "script.py"))