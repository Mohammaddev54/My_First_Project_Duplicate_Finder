"""
Author/Programmer: https://github.com/Mohammaddev54/Mohammaddev54
Project: Duplicate Searching Application
Version: 8
Changes: Improving the readability of the code
"""
#DON' worry about these
"""'sha224', 'sha512_224', 'shake_128', 'sha1', 'sha3_384', 'ripemd160', 'sha512', 'blake2s'
, 'sha384', 'md5-sha1', 'sha256', 'sha512_256', 'sha3_512', 'blake2b', 'shake_256', 'md5'
, 'sha3_224', 'sm3', 'sha3_256'"""
import hashlib
from os import makedirs
from shutil import move
from tkinter import messagebox

# Missing code Function
def not_implemented(self, location):
    print(f"{location}: Code Missing!")

# Percentage Function
def percentage(total, number):
    return int((number * 100) / total)

if __name__ == "__main__":
    print("RUNNING My_Functions.py on Terminal")
"""
Project: Duplicate searching application,
Version: 7
"""

# Necessary Modules
from DUPLICATE_FINDER_GUI_SCRIPT import Duplicate_Finder_GUI
from My_Functions import my_functions as func
from threading import Thread, Event
from os import path, listdir


class Extend_Duplicate_Finder_GUI(Duplicate_Finder_GUI):
    def __init__(self):
        super().__init__()
        self.root.bind("<Escape>", lambda event: self.root.destroy())
        self.root.bind("<Return>", lambda event: self.search_button_action())
        
        # Instance Variables
        self.source = None
        self.destination = None
        self.stop_event = Event()
    
    
    def activate_search_button(self):
        self.search_button.config(state="normal")
    
    
    def deactivate_search_button(self):
        self.search_button.config(state="disabled")

    
    def list_files(self, target):
        return listdir(target)

    def end_of_process(self, process):
        self.root.bind("<Return>", lambda event: self.search_button_action())
        self.activate_search_button()
        print(f"{process}")
        print("--------------------"*5)
        
        self.activate_search_button()
 
    # Main
    def start_scanning(self, folder_name):
        print(f"Scanning ({folder_name}) Directory!")
        
        # If Folder is empty stop
        if self.check_for_empty_folder(folder_name):
            return
        else:
            # scan process
            self.process()

    # Cancel button Function
    def cancel_button_action(self):
        self.stop_event.set()
        func.show_info("Process Canceled")
        self.activate_search_button()
        self.root.bind("<Return>")
    
    def move_files_back_to_source(self):
        source = self.destination
        destination = self.source
        destination_Folder_name = path.basename(destination)
        for file_name in self.list_files(source):
            if self.stop_event.is_set():
                print("UNDO Thread Stopped!")
                break
            print(f"Moving {file_name} Back to ({destination_Folder_name}) Directory!")
            func.move_func(f"{source}/{file_name}", destination)
        else:
            self.end_of_process("UNDO Process is Finished!")
    
    # Undo button Function
    def undo_button_action(self):
        thread_undo = Thread(target=self.move_files_back_to_source(), daemon = True)
        thread_undo.start()

# Initializing Window
window = Extend_Duplicate_Finder_GUI()
window.root.mainloop()
