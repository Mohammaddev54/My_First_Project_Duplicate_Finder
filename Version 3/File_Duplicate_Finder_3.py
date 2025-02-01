# Importing Modules Needed
import os
import hashlib


# Hashing Function
def hash_file(file_path, algorithm="md5"):
    hash_obj = hashlib.new(algorithm)
    if not os.path.isfile(file_path):
        return None
    else:
        with open(file_path, 'rb') as file:
            while chunk:= file.read(8192):
                hash_obj.update(chunk)
            return hash_obj.hexdigest()


def create_new_directory(name):
    if not os.path.exists(name):
        try:
            os.mkdir(name)
        except FileExistsError:
            print(f"Directory {name} Already exists!")
        except Exception as error:
            print(error)
    else:
        print(f"Directory: {name} Created!")

#FOLDER_Name = "DUPLICATES"
#create_new_directory(FOLDER_Name)


# Absolute Path To The Directory/Folder You Want To Search
# Also Listing All The Files On That Folder
source_path = os.getcwd()
'''destination = f"path/{FOLDER_Name}"
os.chdir(source_path)
DIRECTORY = os.listdir(source_path)


# i Is Just A Counter To Keep Track Of The Process
# hashes Is A Dictionary To Store All The Hashes Of All Files In The Directory/Folder
i = 0
hashes = {}


# try w/ except Block Of Code To Catch Any Errors That May Occur
try:
    # Main
    # Going Through All The Files And Checking If It Already Exists In hashes Dictionary
    for f in DIRECTORY:
            i += 1
            
            src_path = os.path.join(source_path, f)
            dst_path = os.path.join(destination, f)
            file_path = os.path.join(source_path, f)
            
            hash_of_file = hash_file(file_path)
            
            # If Not Adding That File To That Hashes Dictionary
            if hash_of_file not in hashes:
                hashes[hash_of_file] = file_path
                print(f"{i} N\\A")
            
            else:
                os.rename(src_path, dst_path)
            
            # Under Commented for now
            # Else Will Write A Log To Save Any Duplicates
                #with open("LOG.txt", 'a') as logfile:
                #    logfile.write(f"{i} {f}, \t address: {file_path}, \t hash_value:{hash_of_file}\n\n")
# Catching Any Exceptions
except Exception as error:
    print(f"{error} has happend in {file_path})")

# Finally Printing Completed In Terminal When Process Is Finished
finally:
    print("Completed")'''
    

print(source_path)
