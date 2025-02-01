import os
import hashlib

def hash_file(file_path, algorithm="md5"):
    hash_obj = hashlib.new(algorithm)
    
    with open(file_path, 'rb') as file:
        while chunk:= file.read(8192):
            hash_obj.update(chunk)
        return hash_obj.hexdigest()

def duplicate_checker(file1, file2):
    return True if file1 == file2 else False

#  "D:\\Photos\\photo\\DCIM\\Camera"

DIRECTORY_PATH = "E:\\Programming\\pictures"
DIRCTORY = os.listdir(DIRECTORY_PATH)
i = 0

for index, file_1 in enumerate(DIRCTORY[:]):
    try:
        is_duplicate = False
        file_1_path = os.path.join(DIRECTORY_PATH, file_1)
        
        hashed_file_1 = hash_file(file_1_path)
        if not hashed_file_1:
            continue
        
        for file_2 in DIRCTORY[index + 1:]:
            i += 1
            file_2_path = os.path.join(DIRECTORY_PATH, file_2)
            
            hashed_file_2 = hash_file(file_2_path)
            if not hashed_file_2:
                continue
        
            if duplicate_checker(hashed_file_1, hashed_file_2):
                is_duplicate = True
                with open("LOG.txt", 'a') as logfile:
                    logfile.write(f"{i} Match found for {file_1} with {file_2}\n")
                    DIRCTORY.remove(file_2)
            else:
                print(f"{i} N\\A")
    except Exception as error:
        with open("LOG.txt", 'a') as logfile:
            logfile.write(f"{i} Error with {file_1} in : {error}\n")
else:
    print("Process Completed")
        