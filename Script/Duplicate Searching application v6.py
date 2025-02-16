"""
Project: Duplicate searching application,
Version: 6
"""

# Necessary Modules
from DUPLICATE_FINDER_GUI_SCRIPT import Duplicate_Finder_GUI
from threading import Thread
from os import path, listdir
from tkinter import ttk, messagebox
from tkinter import *
import hashlib


class Extend_Duplicate_Finder_GUI(Duplicate_Finder_GUI):
    
    
    def __init__(self):
        super().__init__()
        self.root.bind("<Escape>", lambda event: self.root.destroy())
        '''Enabling Searching action by pressing (Return/Enter) key on Keyboard. --NOT RECOMENDED RIGHT NOW-- '''
        #self.root.bind("<Return>", lambda event: self.search_button_action())
        
        self.source = None
        self.destination = None
    
    
    # Error Info Window
    def error_messagebox(self, error):
        messagebox.showinfo("ERROR", error)
    
    
    def function_hash(self, file_path, algorithm="md5"):
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
        try:
            raise NotImplementedError("Code Missing...")
        except NotImplementedError as e:
            print(f"{location}: {e}")
    
    # Main
    def start_scanning(self, folder_name):
        print(f"Scanning {folder_name} Directory!")
        files = listdir(self.source)
        x = []
        for self.file_name in files:
            self.file_name_path = path.join(self.source, self.file_name)
            if not path.isfile(self.file_name_path):
                print(f"Folder detected: {path.basename(self.file_name_path)}")
                continue
            self.hash_key = self.function_hash(self.file_name_path)
            if self.hash_key not in x:
                x.append(self.hash_key)
            else:
                print(f"{self.hash_key}: {self.file_name} is a duplicate!")
        else:
            print("Task completed!")
    
    # Fetching Input Info
    def get_input_information(self):
        data = [self.source_entry, self.destination_entry]
        self.source, self.destination = list(datum.get().replace("\\", '/') if datum != '' else None for datum in data)
        if path.exists(self.source) is False:
            self.error_messagebox("Invalid Source")
        else:
            self.search_button.config(state="disabled")
            self.start_scanning(path.basename(self.source))
    
    # Search button Function
    def search_button_action(self):
        self.get_input_information()
        
    # Undo button Function
    def undo_button_action(self):
        self.not_implemented("btn_undo_action")
    
    # Cancel button Function
    def cancel_button_action(self):
        self.not_implemented("btn_cancel_action")


# Initializing Window
window = Extend_Duplicate_Finder_GUI()
window.root.mainloop()
