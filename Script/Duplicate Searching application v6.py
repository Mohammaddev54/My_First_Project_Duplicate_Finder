"""
Project: Duplicate searching application,
Version: 6,
DUPLICATE_FINDER_GUI_SCRIPT should be in the same Directory/Folder with Duplicate Searching application script
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
    
    
    # Main
    def start_scanning(self, folder_name):
        
        x = []
        files = listdir(self.source)
        print(f"Scanning ({folder_name}) Directory!")
        
        # If Folder is empty stop
        if not files:
            print(f"{folder_name} is Empty")
            print("--------------------"*5)
            self.search_button.config(state="normal")
            return
        else:
            # scan process
            for file_name in files:
                
                if self.stop_event.is_set():
                    print("thread stopped")
                    break
                    
                self.file_name_path = path.join(self.source, file_name)
                
                if not path.isfile(self.file_name_path):
                    print(f"FOLDER: {file_name}")
                    continue
                
                self.hash_key = func.function_hash(self.file_name_path)
                
                if self.hash_key not in x:
                    print(f"{self.hash_key}: {file_name}")
                    x.append(self.hash_key)
                else:
                    func.move_func(f"{self.source}/{file_name}", self.destination)
            
            else:
                self.root.bind("<Return>", lambda event: self.search_button_action())
                self.search_button.config(state="normal")
                print("--------------------"*5)
    
    
    # Search button's Function
    def search_button_action(self):
        data = (self.source_entry, self.destination_entry)
        
        self.source, self.destination = [datum.get().replace("\\", '/') \
            if datum.get() != '' else "" for datum in data]
        
        if path.exists(self.source) is False:
            func.show_error("Invalid Source")
        else:
            if self.destination == "":
                func.create_folder(self.source)
                self.destination = f"{self.source}/Dupelicates"
            self.root.unbind("<Return>")
            self.search_button.config(state="disabled")
            
            self.stop_event.clear()
            
            thread_1 = Thread(target=self.start_scanning, \
                args=(path.basename(self.source),), daemon = True)
            
            thread_1.start()
    
    # Cancel button Function
    def cancel_button_action(self):
        self.stop_event.set()
        print("cancel clicked")
        self.search_button.config(state="normal")
        self.root.bind("<Return>")
    
    # Undo button Function
    def undo_button_action(self):
        self.not_implemented("btn_undo_action")

# Initializing Window
window = Extend_Duplicate_Finder_GUI()
window.root.mainloop()
