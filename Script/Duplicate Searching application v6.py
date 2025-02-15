"""
Project: Duplicate searching application,
Version: 6,
DUPLICATE_FINDER_GUI_SCRIPT should be in the same Directory/Folder with Duplicate Searching application script
"""

# Necessary Modules
from DUPLICATE_FINDER_GUI_SCRIPT import Duplicate_Finder_GUI
from tkinter import *
from tkinter import ttk, messagebox
from threading import Thread
import os

class Extend_Duplicate_Finder_GUI(Duplicate_Finder_GUI):
    
    
    def __init__(self):
        super().__init__()
        self.root.bind("<Escape>", lambda event: self.root.destroy())
        self.root.bind("<Return>", lambda event: self.btn_search_action())
        
        self.source = None
        self.destination = None
    
    
    def error_messagebox(self, error):
        messagebox.showinfo("ERROR", error)
    
    
    # Missing code Function
    def not_implemented(self, location):
        try:
            raise NotImplementedError("Code Missing...")
        except NotImplementedError as e:
            print(f"{location}: {e}")
    
    def get_input_information(self):
        data = [self.source_entry, self.destination_entry]
        self.source, self.destination = list(datum.get().replace("\\", '/') if datum != '' else None for datum in data)
        if os.path.exists(self.source) is False:
            self.error_messagebox("Invalid Source")
        else:
            self.search_button.config(state="disabled")
            print("STARTED!")
    
    
    def btn_search_action(self):
        self.get_input_information()
        
    
    def btn_undo_action(self):
        self.not_implemented("btn_undo_action")
    
    
    def btn_cancel_action(self):
        self.not_implemented("btn_cancel_action")

window = Extend_Duplicate_Finder_GUI()
window.root.mainloop()
