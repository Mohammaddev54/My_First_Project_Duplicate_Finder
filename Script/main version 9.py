"""
Author/Programmer: https://github.com/Mohammaddev54/Mohammaddev54
Project: Duplicate Files Searching Application
Version: 9
"""
from os import path, listdir, rmdir, makedirs, system
from shutil import move
import hashlib
from threading import Thread, Event
from tkinter import messagebox, filedialog, END
from GuiScript import Window # type: ignore

class ApplicationWindow(Window):
    def __init__(self):
        super().__init__()
        self.root.bind("<Escape>", lambda event: self.root.destroy())
        self.root.bind("<Return>", lambda event: self.search_button_action())
        self.file_menu.add_command(label="Set Source", command=self.set_source_entry)
        self.file_menu.add_command(label="Set Destination", command=self.set_destination_entry)
        self.file_menu.add_command(label="Exit", command=quit)
        self.help_menu.add_command(label="Github repository", command=lambda: system("start https://github.com/Mohammaddev54/My_First_Project_Duplicate_Finder"))
        self.about = "More Info on Github\nProgrammed in: Python 3.13.5\nAuthor: Mohammad_Dev\nVersion: 9"
        self.help_menu.add_command(label="About", command=lambda: self.show_info(self.about, title="About"))
    
    
    def set_source_entry(self):
        file_path = FileHandler.get_file_path(self)
        self.source_entry.delete(0, END)
        self.source_entry.insert("1", file_path)
    
    def set_destination_entry(self):
        file_path = FileHandler.get_file_path(self)
        self.destination_entry.delete(0, END)
        self.destination_entry.insert("1", file_path)
    
    def reset_processed_file_lbl(self):
        self.lbl_processed_file.config(text="")

    @staticmethod
    def show_info(message, title="INFO"):
        messagebox.showinfo(title=title, message=message)

    @staticmethod
    def show_error(error):
        messagebox.showerror("ERROR", error)
    
    def get_source_path(self):
        return self.source_path
    
    def get_destination_path(self):
        if self.destination_path == "N\\A":
            self.destination_path = path.join(self.source_path, "Duplicates")
        return self.destination_path
    
    def activate_button(self, button_name):
        button_name.config(state="normal")

    def deactivate_button(self, button_name):
        button_name.config(state="disabled")

    def activate_key(self, key_name):
        self.root.bind(key_name, lambda event: self.search_button_action())
    
    def deactivate_key(self, key_name):
        self.root.unbind(key_name)
    
    def cancel_button_action(self):
        MyThreadManager.stop_event.set()
        self.activate_button(self.undo_button)
    
    def undo_button_action(self):
        Main.undo_function(self)
    
    def search_button_action(self):
        # Get data from entry/input boxes
        data = (self.source_entry, self.destination_entry)
        self.source_path = data[0].get().strip().replace("\\", "/")
        self.source_path = self.source_path if self.source_path else "N\\A"
        self.destination_path = data[1].get().strip().replace("\\", '/')
        self.destination_path = self.destination_path if self.destination_path else "N\\A"
    
        # Backend
        Main.start(self)


class Main():
    def undo_function(instance):
        if path.isdir(instance.destination_path):
            files = listdir(instance.destination_path)
            instance.deactivate_button(instance.search_button)
            instance.deactivate_key("<Return>")
            undoing = lambda files: Main.run_undo_process(instance, files)
            MyThreadManager.create_thread("UNDO_PROCESS", undoing, (files,))
        else:
            ApplicationWindow.show_error(f"{instance.destination_path} Doesn't Exist")
    
    def start(instance):
        # Throw and error if the source path is not valid
        if not FileHandler.check_for_valid_path(instance.source_path):
            ApplicationWindow.show_error(f"Invalid source path: {instance.source_path}")
        else:
            instance.deactivate_key("<Return>")
            instance.deactivate_button(instance.undo_button)
            instance.deactivate_button(instance.search_button)
            instance.activate_button(instance.cancel_button)
            # Checking if destination is valid
            if not FileHandler.file_is_folder(instance.destination_path):
                FileHandler.create_folder(instance.source_path, folder_name="Duplicates")
                instance.destination_path = path.join(instance.source_path, "Duplicates")
            # Doing some more checks on source path
            if FileHandler.file_check_list(instance.source_path):
                files = listdir(instance.source_path)
            thread_process = lambda files: Main.run_process(instance, files)
            MyThreadManager.create_thread("main_process", thread_process, (files,))

    def run_undo_process(instance, files):
        Scanner.undo_process(instance, files)
        instance.activate_key("<Return>")
        instance.activate_button(instance.search_button)

    def run_process(instance, files):
        Scanner.process(instance, files)
        instance.activate_key("<Return>")
        instance.activate_button(instance.search_button)
        instance.deactivate_button(instance.cancel_button)


class FileHandler():
    def get_file_path(self):
        return str(filedialog.askdirectory(initialdir=self.current_directory))
    @staticmethod
    def delete_file(file_path):
        rmdir(file_path)
    
    @staticmethod
    def move_func(file_path, destination_path):
        try:
            move(file_path, destination_path)
        except Exception as error:
            ApplicationWindow.show_error(error)
    
    @staticmethod
    def create_folder(Directory_path, folder_name):
        dir = F"{Directory_path}/{folder_name}"
        makedirs(dir, exist_ok = True)
    
    @staticmethod
    def file_is_folder(file_path):
        return path.isdir(file_path)

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
        if FileHandler.check_for_empty_folder(file_path):
            print("empty folder")
            return False
        elif not FileHandler.is_file_folder(file_path):
            print("File is folder")
            return False
        else:
            return True


class Scanner():
    @staticmethod
    def hash_function(file_path, algorithm="sha3_256"):
        hash_object = hashlib.new(algorithm)
        try:
            with open(file_path, "rb") as file:
                while chunk:= file.read(8192):
                    hash_object.update(chunk)
            return hash_object.hexdigest()
        except Exception as error:
            ApplicationWindow.show_error(error)
    
    def undo_process(instance, files):
        for file_name in files:
                source_path = instance.get_destination_path()
                destination_path = instance.get_source_path()
                file_name_path = path.join(source_path, file_name)
                instance.lbl_processed_file.config(text=f"Moved back{file_name}", fg="orange")
                FileHandler.move_func(file_name_path, destination_path)
        else:
            ApplicationWindow.show_info("Undo Finished")
            ApplicationWindow.reset_processed_file_lbl(instance)
    
    def process(instance, files):
        hashed_data = {}
        for file_name in files:
            # ONLY HAPPENS WHEN CANCEL IS CLICKED
            if MyThreadManager.stop_event.is_set():
                MyThreadManager.stop_event.clear()
                ApplicationWindow.reset_processed_file_lbl(instance)
                instance.activate_key("<Return>")
                instance.activate_button(instance.search_button)
                break
            else:
                source_path = instance.get_source_path()
                destination_path = instance.get_destination_path()
                file_name_path = path.join(source_path, file_name)
                
                if FileHandler.is_file_folder(file_name_path):
                    continue
                else:
                    hashed_file = Scanner.hash_function(file_name_path)
                    if hashed_file not in hashed_data.keys():
                        instance.lbl_processed_file.config(text=file_name, fg="Green")
                        hashed_data[hashed_file] = file_name
                    else:
                        instance.lbl_processed_file.config(text=f"Duplicate:  {file_name}", fg="Red")
                        FileHandler.move_func(file_name_path, destination_path)
        else:
            ApplicationWindow.reset_processed_file_lbl(instance)
            instance.activate_button(instance.undo_button)
            ApplicationWindow.show_info("Process Finished")
            if not FileHandler.check_for_valid_path(destination_path):
                print("Not Valid")
                return
            if FileHandler.check_for_empty_folder(destination_path):
                FileHandler.delete_file(destination_path)
                instance.deactivate_button(instance.undo_button)


class MyThreadManager():
    stop_event = Event()
    stop_event.clear()
    thread_dictionary = {}
    
    @staticmethod
    def stop_thread():
        MyThreadManager.stop_event.set()
    
    @staticmethod
    def create_thread(thread_name, thread_function, arguments):
        thread = Thread(target = thread_function, args = arguments, daemon = True)
        thread.name = thread_name
        thread.start()
        MyThreadManager.thread_dictionary[thread_name] = thread
    
    @staticmethod
    def get_thread(thread_name):
        return MyThreadManager.thread_dictionary[thread_name]


if __name__ == '__main__':
    window = ApplicationWindow()
    window.root.mainloop()
