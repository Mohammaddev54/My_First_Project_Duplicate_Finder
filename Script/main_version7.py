"""
Author/Programmer: https://github.com/Mohammaddev54/Mohammaddev54
Project: Duplicate Searching Application
Version: 8
 
Description of changes made:
- I've tried to implement the SRP(Single Responsibilty Principle)
- The cancel_button & undo_button functions' have been removed going to be added later
- Refactoring all code
- Variable name changes
- In total I would say Improvements on structure of the script
"""

from gui_script import win
from os import path, listdir, makedirs
from threading import Thread, Event
from tkinter import messagebox
from shutil import move
import hashlib

class window(win):
    # Initialize winodow
    def __init__(self):
        super().__init__()
        self.root.bind("<Escape>", lambda event: self.root.destroy())
        self.root.bind("<Return>", lambda event: self.search_button_action())
        
    # Info window
    @staticmethod
    def show_info(info):
        messagebox.showinfo("INFO", info)

    # ERROR window
    @staticmethod
    def show_error(error):
        messagebox.showerror("ERROR", error)
    
    # Get Source path    
    def get_source_path(self):
        return self.source_path
    
    # Get destination path
    def get_destination_path(self):
        if self.destination_path == "N\\A":
            self.destination_path = path.join(self.source_path, "Duplicates")
        return self.destination_path
    
    # Activate a Button on Screen
    def activate_button(self, button_name):
        button_name.config(state="normal")

    # Deactivate a Button on Screen
    def deactivate_button(self, button_name):
        button_name.config(state="disabled")

    # Activate a keyboard key    
    def activate_key(self, key_name):
        self.root.bind(key_name, lambda event: self.search_button_action())
    
    # Deactivate a keyboard key
    def deactivate_key(self, key_name):
        self.root.unbind(key_name)
    
    # Search button's Function
    def search_button_action(self):
        # Get data from entry/input boxes
        data = (self.source_entry, self.destination_entry)
        self.source_path = data[0].get().strip().replace("\\", "/")
        self.source_path = self.source_path if self.source_path else "N\\A"
        self.destination_path = data[1].get().strip().replace("\\", '/')
        self.destination_path = self.destination_path if self.destination_path else "N\\A"
        
        # Backend
        duplicate_finder_app.run(self)
    
    # Cancel button's Function
    def cancel_button_action(self):
        raise NotImplementedError

class duplicate_finder_app():
    '''These are some Pre running checks that user inputs/source_path
    & destination_path go through before running the program!'''
    # This try-except block is for unknown errors that can occur
    try:
        # run the main process
        @staticmethod
        def run(self):
            # Throw and error if the source path is not valid
            if not file_handler.check_for_valid_path(self.source_path):
                window.show_error(f"Invalid source path: {self.source_path}")
            
            else:
                
                self.deactivate_key("<Return>")
                self.deactivate_button(self.search_button)
                self.activate_button(self.cancel_button)
                
                # Checking if destination is valid
                if not file_handler.check_for_valid_path(self.destination_path):
                    file_handler.create_folder(self.source_path, folder_name="Duplicates")
                    
                    # Doing some more checks on source path
                    if file_handler.file_check_list(self.source_path):
                        files = listdir(self.source_path)
                    process = lambda files: duplicate_finder_app.process(self, files)
                    thread_manager.create_thread("main_process", process, (files,))
        
        # main process app
        @staticmethod
        def process(self, files):
            duplicate_scanner.process(self, files)
            self.activate_key("<Return>")
            self.activate_button(self.search_button)
    except Exception as error:
        window.show_error(error)
# File creation, moving...
class file_handler():
    
    # Move Function
    @staticmethod
    def move_func(file_path, destination_path):
        try:
            move(file_path, destination_path)
        except Exception as error:
            window.show_error(error)
    
    # Folder Creating Function
    @staticmethod
    def create_folder(Directory_path, folder_name):
        dir = F"{Directory_path}/{folder_name}"
        makedirs(dir, exist_ok = True)
    
    @staticmethod
    def check_for_valid_path(file_path):
        return path.exists(file_path)
    
    @staticmethod
    def check_for_empty_folder(file_path):
        if not listdir(file_path):
            return True
        else:
            return False
    
    @staticmethod
    def is_file_folder(file_path):
        if not path.isfile(file_path):
                return True
        else:
            return False
    
    @staticmethod
    def file_check_list(file_path):
        if file_handler.check_for_empty_folder(file_path):
            print("empty folder")
            return False
        elif not file_handler.is_file_folder(file_path):
            print("File is folder")
            return False
        else:
            return True
# Scanning for duplicates
class duplicate_scanner():
    
    # Hashing Function
    @staticmethod
    def hash_function(file_path, algorithm="sha3_256"):
        hash_object = hashlib.new(algorithm)
        try:
            with open(file_path, "rb") as file:
                while chunk:= file.read(8192):
                    hash_object.update(chunk)
            return hash_object.hexdigest()
        except Exception as error:
            window.show_error(error)
    
    @staticmethod
    def process(self, files):
        x = {}
        for file_name in files:
            # ONLY HAPPENS WHEN CANCEL IS CLICKED
            if thread_manager.stop_event.is_set():
                thread_manager.stop_event.clear()
                self.activate_key("<Return>")
                self.activate_button(self.search_button)
                break
            else:
                
                source_path = self.get_source_path()
                destination_path = self.get_destination_path()
                file_name_path = path.join(source_path, file_name)
                
                if file_handler.is_file_folder(file_name_path):
                    continue
                else:
                    hashed_data = duplicate_scanner.hash_function(file_name_path)
                    
                    if hashed_data not in x.keys():
                        print(file_name)
                        x[hashed_data] = file_name
                    else:
                        print(f"{file_name} moved!")
                        file_handler.move_func(file_name_path, destination_path)
        else:
            print("Process Ended!")
# Manage, Create, Start, Stop a thread
class thread_manager():
    
    stop_event = Event()
    stop_event.clear()
    thread_dictionary = {}
    
    @staticmethod
    def stop_thread():
        thread_manager.stop_event.set()
    
    @staticmethod
    def create_thread(thread_name, thread_function, arguments):
        thread = Thread(target = thread_function, args = arguments, daemon = True)
        thread.name = thread_name
        thread.start()
        thread_manager.thread_dictionary[thread_name] = thread
    
    @staticmethod
    def get_thread(thread_name):
        return thread_manager.thread_dictionary[thread_name]
    
# if it is run on terminal
if __name__ == "__main__":
    Window = window()
    Window.root.mainloop()
