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
    
    
    def check_for_empty_folder(self, folder_name):
        if not self.list_files(self.source):
            print("Folder is Empty!")
            print("--------------------"*5)
            self.activate_search_button()
            return True
        else:
            return False
    
    
    def file_is_folder(self, file_name, file_name_path):
        if not path.isfile(self.file_name_path):
                print(f"FOLDER: {file_name}")
                return True
        else:
            return False
    
    
    def end_of_process(self, process):
        self.root.bind("<Return>", lambda event: self.search_button_action())
        self.activate_search_button()
        print(f"{process}")
        print("--------------------"*5)
        
        self.activate_search_button()
    
    
    def process(self):
        x = {}
        for file_name in self.list_files(self.source):
                
                if self.stop_event.is_set():
                    print("Process Thread Stoped!")
                    break
                    
                self.file_name_path = path.join(self.source, file_name)
                
                if self.file_is_folder(file_name, self.file_name_path):
                    continue
                
                self.hash_key = func.function_hash(self.file_name_path)
                
                if self.hash_key not in x.keys():
                    print(f"{self.hash_key}: {file_name}")
                    x[self.hash_key] = file_name
                else:
                    func.move_func(f"{self.source}/{file_name}", self.destination)
            
        else:
            self.end_of_process("Process Ended!")
    
    # Main
    def start_scanning(self, folder_name):
        print(f"Scanning ({folder_name}) Directory!")
        
        # If Folder is empty stop
        if self.check_for_empty_folder(folder_name):
            return
        else:
            # scan process
            self.process()
    
    
    def check_for_valid_path(self):
        if path.exists(self.source) is False:
            return True
        else:
            return False
    
    
    # Search button's Function
    def search_button_action(self):
        data = (self.source_entry, self.destination_entry)
        
        self.source, self.destination = [datum.get().replace("\\", '/') \
            if datum.get() != '' else "" for datum in data]
        
        if self.check_for_valid_path():
            func.show_error("Invalid Source")
        else:
            if self.destination == "":
                func.create_folder(self.source)
                self.destination = f"{self.source}/Dupelicates"
            
            self.root.unbind("<Return>")
            self.deactivate_search_button()
            self.stop_event.clear()
            
            thread_process = Thread(target=self.start_scanning, \
                args=(path.basename(self.source),), daemon = True)
            
            thread_process.start()
    
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
