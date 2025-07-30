from os import getcwd, path
from tkinter import ttk, Tk, Label, Entry, Button, Menu


class Window:
    def __init__(self, root=None):
        if root is None:
            root = Tk()
        self.root = root

        self.current_directory = getcwd()
        path_to_icon = path.join(self.current_directory, "Images", "duplicate_file_icon.ico")
        self.root.iconbitmap(path_to_icon)

        self.root.geometry("500x370")
        self.root.title("Search Duplicates")
        self.root.resizable(False, False)

        # Uncomment if needed
        # self.root.bind("<Escape>", lambda event: self.root.destroy())
        # self.root.bind("<Return>", lambda event: self.search_button_action())

        # Menu bar
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)
        self.file_menu = Menu(self.menubar, tearoff=0)
        self.help_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.menubar.add_cascade(label="Help", menu=self.help_menu)

        # Frames
        self.top_frame = ttk.Frame(self.root, padding=10, borderwidth=2, relief="solid")
        self.middle_frame = ttk.Frame(self.root, padding=10, borderwidth=2, relief="solid")
        self.bottom_frame = ttk.LabelFrame(self.root, text="Processed: ", padding=10)

        self.top_frame.pack(padx=10, pady=10, fill="x")
        self.middle_frame.pack(padx=10, pady=10, fill="x")
        self.bottom_frame.pack(padx=10, pady=10, expand=True, fill="both")

        # Bottom frame label
        self.lbl_processed_file = Label(self.bottom_frame, text="", width=40, wraplength=300)
        self.lbl_processed_file.pack()

        # Top frame labels
        self.lbl_source = Label(self.top_frame, text="Source", pady=10, padx=10, font=(14))
        self.lbl_destination = Label(self.top_frame, text="Destination", pady=10, padx=10, font=(14))

        self.lbl_source.grid(row=0, column=0)
        self.lbl_destination.grid(row=1, column=0)

        # Entry fields
        self.source_entry = Entry(self.top_frame, width=50)
        self.destination_entry = Entry(self.top_frame, width=50)

        self.source_entry.grid(row=0, column=1, ipadx=5, ipady=5)
        self.destination_entry.grid(row=1, column=1, ipadx=5, ipady=5)

        # Buttons
        self.search_button = Button(
            self.top_frame, text="Search", pady=5, padx=5, font=(14), command=self.search_button_action
        )
        self.undo_button = Button(
            self.middle_frame, text="Undo", pady=5, padx=5, font=(14), state="disabled", command=self.undo_button_action
        )
        self.cancel_button = Button(
            self.middle_frame, text="Cancel", pady=5, padx=5, font=(14), state="disabled", command=self.cancel_button_action
        )

        self.search_button.grid(row=2, column=0)
        self.undo_button.grid(row=0, column=0, padx=10)
        self.cancel_button.grid(row=0, column=1, padx=10)

    # Missing code function
    def not_implemented(self, location):
        print(f"{location}: Code Missing!")

    def search_button_action(self):
        pass

    def undo_button_action(self):
        pass

    def cancel_button_action(self):
        pass


if __name__ == "__main__":
    print("gui running in terminal")
    window = Window()
    window.root.mainloop()
