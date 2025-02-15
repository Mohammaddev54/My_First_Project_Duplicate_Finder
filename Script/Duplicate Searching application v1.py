"""
Project: Duplicate searching application,
Version: 1,
Explination on how script works: This script is the basic searching algorithm with performance of o(n^2) which is not good
this script takes an absolute path to the folder you are going to search in; Then it takes one file and opens it in binary
then compares it's content to the content of other files and displays the result in terminal,
this process is performed till the last file of that folder; Then the second file is scand and etc.
"""

# Using Os module to list all files in a directory
import os

# DIRECTORY  should be an absolute path to the Folder you are searching for!
DIRECTORY = ""
files = os.listdir(DIRECTORY)

# Main
for file1 in files:
    path_to_file1 = f"{DIRECTORY}\\{file1}"
    with open(path_to_file1, 'rb') as first_file:
        content_first_file = first_file.readlines()
        for file2 in files[files.index(file1):]:
            path_to_file2 = f"{DIRECTORY}\\{file2}"
            with open(path_to_file2, 'rb') as second_file:
                content_second_file = second_file.readlines()
                if content_first_file == content_second_file:
                    print(f"{file2} is a duplicate for {file1}!")
                else:
                    print(f"{file2} is not a duplicate!")
