import tkinter as tk
from tkinter import simpledialog

class PasswordEntry(simpledialog.Dialog):
    def __init__(self, parent, selected_item=None):
        self.selected_item = selected_item
        super().__init__(parent)

    def body(self, master):
        # Create labels and entries for site, username, and password
        tk.Label(master, text="Site:").grid(row=0)
        tk.Label(master, text="Username:").grid(row=1)
        tk.Label(master, text="Password:").grid(row=2)

        self.site_entry = tk.Entry(master)
        self.username_entry = tk.Entry(master)
        self.password_entry = tk.Entry(master, show="*")

        self.site_entry.grid(row=0, column=1)
        self.username_entry.grid(row=1, column=1)
        self.password_entry.grid(row=2, column=1)

        # If editing an existing entry, populate the fields
        if self.selected_item:
            site, username = self.selected_item.split(" - ")
            self.site_entry.insert(0, site)
            self.username_entry.insert(0, username)

        return self.site_entry  # Focus on the site entry

    def apply(self):
        # Get the data from the entries
        self.site = self.site_entry.get()
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()