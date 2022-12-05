import os

comments = "A test of file size"

def CheckFileSize(filename):
    with open(filename, "w") as file:
        file.write(comments)


    file_size = os.path.getsize(filename)
    return(file_size)


print(CheckFileSize("test.txt"))