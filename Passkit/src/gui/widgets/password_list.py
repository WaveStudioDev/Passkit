import tkinter as tk
from tkinter import Listbox, Scrollbar

class PasswordList(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        # Create a listbox for displaying passwords
        self.listbox = Listbox(self, selectmode=tk.SINGLE)
        self.scrollbar = Scrollbar(self, command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        # Pack the widgets
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def populate(self, passwords):
        """Populate the listbox with password entries."""
        self.listbox.delete(0, tk.END)  # Clear existing items
        for password in passwords:
            self.listbox.insert(tk.END, f"{password['site']} - {password['username']}")

    def get_selected_item(self):
        """Return the selected password entry."""
        try:
            index = self.listbox.curselection()[0]
            return self.listbox.get(index)
        except IndexError:
            return None