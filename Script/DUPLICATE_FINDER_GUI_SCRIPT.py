'''
GUI setup script for duplicate Searching application.
'''

from tkinter import *
from tkinter import ttk

class Duplicate_Finder_GUI():
    def __init__(self, root=None):
        
        if root == None:
            root = Tk()
            self.root = root
        else:
            self.root = root
        
        self.root.geometry("500x320")
        self.root.title("Search Duplicates")
        self.root.resizable(False, False)
        
        self.top_frame         = ttk.Frame(self.root, padding = (10), borderwidth = 2, relief="solid")
        self.bottom_frame      = ttk.Frame(self.root, padding = (10), borderwidth = 2, relief="solid")
        
        self.lbl_source        =      Label(self.top_frame, text="Source", pady = 10, padx = 10, font=(14))
        self.lbl_destination   = Label(self.top_frame, text="Destination", pady = 10, padx = 10, font=(14))
        
        self.source_entry      = Entry(self.top_frame, width = 50)
        self.destination_entry = Entry(self.top_frame, width = 50)
        
        self.lbl_source.grid(                            row = 0, column = 0)
        self.lbl_destination.grid(                       row = 1, column = 0)
        
        self.source_entry.grid(     row = 0, column = 1, ipadx= 5, ipady = 5)
        self.destination_entry.grid(row = 1, column = 1, ipadx= 5, ipady = 5)
        
        self.search_button      =    Button(self.top_frame, text="Search", pady = 5, padx = 5, font= (14), command = self.search_button_action)
        self.undo_button        =     Button(self.bottom_frame, text="Undo", pady = 5, padx = 5, font= (14), command = self.undo_button_action)
        self.cancel_button      = Button(self.bottom_frame, text="Cancel", pady = 5, padx = 5, font= (14), command = self.cancel_button_action)
        
        self.search_button.grid(           row = 2, column = 0)
        self.undo_button.grid(  row = 0, column = 0, padx = 10)
        self.cancel_button.grid(row = 0, column = 1, padx = 10)
        
        self.top_frame.pack(padx = 10, pady = 10, side = "top", fil  = 'x')
        self.bottom_frame.pack(           padx = 10, pady = 10, fill = 'x')
        
    def search_button_action(self):
        pass
    
    
    def undo_button_action(self):
        pass
    
    
    def cancel_button_action(self):
        pass

if __name__ == "__main__":
    window = Duplicate_Finder_GUI()
    window.root.mainloop()
