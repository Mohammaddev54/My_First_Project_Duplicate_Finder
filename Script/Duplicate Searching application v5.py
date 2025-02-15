"""
Project: Duplicate searching application,
Version: 5,
This program is intented to run on the same Directory as it is scanning which isn't good.
"""

# Necessary Modules
import os
import hashlib
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Global Variables
thread = None
total = 0
processed = 0

# Percentage Function
def percentage(total, number):
    return int((number * 100) / total)

# Error Function
def error_window(error):
    messagebox.showinfo("ERROR", f"Experienced: {error}")

# Duplicate Folder Creating Function
def create_new_Directory(src):
    try:
        if not os.path.exists(src + "/Duplicate"):
            os.makedirs(src + "/Duplicate")
            d = src + "/Duplicate"
            return d
        else: 
            print("Duplicate Folder Already exists")
    except Exception as error:
        error_window(error)

# Hashing Function
def hash_the_file(path_to_file, algorithm = "md5"):
    hash_object = hashlib.new(algorithm)
    if not os.path.isfile(path_to_file):
        pass
    else:
        try:
            with open(path_to_file, "rb") as file:
                while chunk:= file.read(8192):
                    hash_object.update(chunk)
            return hash_object.hexdigest()
        except Exception as error:
            error_window(error)

# Fetching info Function
def get_input_info():
    try:
        s = source_entry.get().replace("\\", "/")
        d = destin_entry.get().replace("\\", "/")
        return s, d
    except Exception as error:
        error_window(error)

# Checking if Inputs are blank
def not_blank():
    return len(source_entry.get()) >= 3

# Updating GUI with the progress of progress bar
def update_progress_bar(t, p):
    progress_bar["value"] = percentage(t, p)

# Start Function for All processes
def start():
    s, d = get_input_info()
    if os.path.exists(d):
        search(s, d)
    else:
        d = create_new_Directory(s)
        search(s, d)

# Searching/Scanning Function
def search(s, d):
    global processed, total
    try:
        ALLFILES = os.listdir(s)
        total = len(ALLFILES)
        all_file_hashes = {}
        for file_name in ALLFILES:
            file_path = os.path.join(s, file_name)
            if not os.path.isfile(file_path):
                pass
            else:
                destination_path = os.path.join(d, file_name).replace("\\", "/")
                hashed_file = hash_the_file(file_path)
                processed += 1
                if hashed_file and hashed_file not in all_file_hashes:
                    all_file_hashes[hashed_file] = file_name
                    print(processed)
                else:
                    print(file_path)
                    os.rename(file_path, destination_path)
                r.after(100, update_progress_bar(total, processed))
        btn_search.config(state="normal")
        messagebox.showinfo("Info", "Search Completed!")
        progress_bar["value"] = 0
    except Exception as error:
        error_window(error)

# Search Button Function
def search_action():
    s, d = get_input_info()
    if os.path.exists(s):#not_blank() and os.path.exists(s)
        btn_search.config(state="disabled")
        thread = Thread(target=start, daemon=True)
        thread.start()
    else:
        error_window("Invalid input! Please provide a valid source Directory.")

# Undo Button Function
def undo_action():
    pass

# Cancel Button Function
def cancel_action():
    pass

# Tkinter setup
r = Tk()
r.title("Duplicate Finder")
r.geometry("500x320")
r.resizable(False, False)

# Layout
top_frame = ttk.Frame(r, padding = "8", borderwidth = 2, relief="groove")
bottom_frame = ttk.Frame(r, padding = "8", borderwidth = 2, relief="groove")

lbl_source = Label(top_frame, text="Source", padx = 5, pady = 5, font=(12))
lbl_source.grid(row = 0, column = 0)

lbl_destin = Label(top_frame, text="Destination", padx = 5, pady = 5, font=(12))
lbl_destin.grid(row = 1, column = 0)

source_entry = Entry(top_frame, width= 50)
source_entry.grid(row = 0, column = 1, padx = 10, pady= 5, ipadx= 3, ipady= 2)

destin_entry = Entry(top_frame, width= 50)
destin_entry.grid(row = 1, column = 1, padx = 10, pady= 5, ipadx= 3, ipady= 2)

btn_search = Button(top_frame, text="Search", font=(12), command=search_action)
btn_search.grid(row = 2, column = 0)

btn_undo = Button(bottom_frame, text="Undo", font=(12))
btn_undo.grid(row = 0, column = 0)

btn_cancel = Button(bottom_frame, text="Cancel", font=(12))
btn_cancel.grid(row = 0, column = 1, padx = 15)

progress_bar = ttk.Progressbar(
    r,
    orient = "horizontal",
    maximum = 100,
    length = 450
)

top_frame.pack(
    padx = 20,
    pady = 20,
    fill = "x",
    side = "top"
)


bottom_frame.pack(
    padx = 20,
    pady = 20,
    fill = "x"
)
progress_bar.pack()

r.bind(r, "<Enter>", lambda:r.destroy())

# Window main loop
r.mainloop()
