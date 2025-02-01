# Importing Modules Needed
import os
import hashlib


# Hashing Function
def hash_file(file_path, algorithm="md5"):
    hash_obj = hashlib.new(algorithm)
    
    with open(file_path, 'rb') as file:
        while chunk:= file.read(8192):
            hash_obj.update(chunk)
        return hash_obj.hexdigest()

# Absolute Path To The Directory/Folder You Want To Search
# Also Listing All The Files On That Folder
DIRECTORY_PATH = ""
DIRCTORY = os.listdir(DIRECTORY_PATH)

# i Is Just A Counter To Keep Track Of The Process
# hashes Is A Dictionary To Store All The Hashes Of All Files In The Directory/Folder
i = 0
hashes = {}

# try w/ except Block Of Code To Catch Any Errors That May Occur
try:
    # Main
    # Going Through All The Files And Checking If It Already Exists In hashes Dictionary
    for f in DIRCTORY:
        i += 1
        
        f_path = os.path.join(DIRECTORY_PATH, f)
        hash_of_file = hash_file(f_path)
        # If Not Adding That File To That Hashes Dictionary
        if hash_of_file not in hashes:
            hashes[hash_of_file] = f_path
            print(f"{i} N\\A")
        # Else Will Write A Log To Save Any Duplicates
        else:
            with open("LOG.txt", 'a') as logfile:
                logfile.write(f"{i} {f}, \t address: {f_path}, \t hash_value:{hash_of_file}\n\n")

# Catching Any Exceptions
except Exception as error:
    print(error)

# Finally Printing Completed In Terminal When Process Is Finished
finally:
    print("Completed")