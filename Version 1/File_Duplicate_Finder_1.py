# Modules needed to run this code
import os
import hashlib


# A function that returns the hash of a file 
# The algorithm can be changed for example: sha256, sha512, md5, ...
def hash_file(file_path, algorithm="md5"):
    hash_obj = hashlib.new(algorithm)
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()


# An absloute path and list of the files in that Directory or folder
DIRECTORY_PATH = "An absloute path to the folder you want to check"
DIRECTORY = os.listdir(DIRECTORY_PATH)


# i is just a counter to keep track of the process
# The loop goes through the Directory/Folder and gets all files with indecies
i = 0
for index, file_1 in enumerate(DIRECTORY):
    # try/except block to catch any potential errors
    try:

        #Geting the absolute path to the file
        file_path_1 = os.path.join(DIRECTORY_PATH, file_1)
        # Getting the hash of that file
        file1 = hash_file(file_path_1)

        # Nested loop to go through every file to check for first file in first loop
        for file_2 in DIRECTORY[index + 1:]:
            i += 1

            file_path_2 = os.path.join(DIRECTORY_PATH, file_2)
            file2 = hash_file(file_path_2)

            # Checking if the both files are the same
            if file1 != file2:
                print(f"{i} No Match!")
            else:
                # Creating and writing log
                with open('log.txt', 'a') as log:
                    log.write(f"{i} MATCH FOUND: [{file_1}], [{file_2}]")

    # Catching any Exceptions
    except Exception as error:
        print(f"ERROR READING FILE IN: {file_1}, {error}")

# Finally printing PROCESS COMPLETED to the terminal
finally:
    print("PROCESS COMPLETED")

# for index, file1 in enumerate(DIRECTORY):
    # try:
        # file_path1 = os.path.join(DIRECTORY_PATH, file1)
        # with open(file_path1, 'rb') as FILE_1:
            # file1_content = FILE_1.read()
            # for file2 in DIRECTORY[index + 1:]:
                # file_path2 = os.path.join(DIRECTORY_PATH, file2)
                # with open(file_path2, 'rb') as FILE_2:
                    # file2_content = FILE_2.read()
                # if file1_content != file2_content:
                    # print(f"No Match found for:  {file1}")
                # else:
                    # print(f"Match found:\t {file1}  :  {file2}")
                    # DIRECTORY.remove(file2)
    # except Exception as err:
        # print(err)
