'''
Project: Duplicate searching application,
My_Functions.py is separating Functions used in main.py,
This Script is add on Version 7!
'''

import hashlib
from os import makedirs
from shutil import move
from tkinter import messagebox

class my_functions:
    
    # Info window
    def show_info(info):
        messagebox.showinfo(f"Tip: {info}")
    
    # ERROR window
    def show_error(error):
        messagebox.showerror("ERROR", error)
    
    # Folder Creating Function
    def create_folder(folder_path, folder_name="Dupelicates"):
        makedirs(f"{folder_path}/{folder_name}", exist_ok = True)
    
    # Move Function
    def move_func(file_path, destination_path):
        try:
            move(file_path, destination_path)
        except Exception as error:
            error_messagebox(error)
    
    # Hashing Function
    def function_hash(file_path, algorithm="md5"):
        hash_object = hashlib.new(algorithm)
        try:
            with open(file_path, "rb") as file:
                while chunk:= file.read(8192):
                    hash_object.update(chunk)
            return hash_object.hexdigest()
        except Exception as error:
            self.error_messagebox(error)
    
    # Missing code Function
    def not_implemented(self, location):
        print(f"{location}: Code Missing!")
    
    # Percentage Function
    def percentage(total, number):
        return int((number * 100) / total)

if __name__ == "__main__":
    print("RUNNING My_Functions.py on Terminal")
