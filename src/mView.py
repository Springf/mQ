import tkinter as tk
from tkinter import ttk


class mView(tk.Frame):
    """A friendly little module"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.name = tk.StringVar()
        self.hello_string = tk.StringVar()
        self.hello_string.set("Question")
        name_label = ttk.Label(self, text="Name:", font=("Calibri", 32))
        name_entry = ttk.Entry(
            self, textvariable=self.name, font=("Calibri", 32))
        hello_label = ttk.Label(self, textvariable=self.hello_string, font=(
            "Calibri", 32), wraplength=1920)
        name_label.grid(row=1, column=0, sticky=tk.W)
        name_entry.grid(row=1, column=1, sticky=(tk.W + tk.E))
        hello_label.grid(row=0, column=0, columnspan=3)
        self.columnconfigure(1, weight=1)
