import tkinter as tk
from tkinter import ttk


class mView(tk.Frame):
    """A friendly little module"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        question_body_frame = tk.LabelFrame(self, text="Question", font=("Calibri", 24))
        self.question_body = tk.StringVar()
        self.question_prompty = tk.StringVar()
        self.question_body.set("23.546 * 12 = ")

        question_body_label = ttk.Label(question_body_frame, textvariable=self.question_body, font=(
            "Calibri", 32), wraplength=1920)
        question_body_frame.grid(row=0, sticky=(tk.W + tk.E), padx=100)
        question_body_label.grid(row=0, sticky=(tk.W + tk.E))
        # name_label.grid(row=1, column=0, sticky=tk.W)
        # name_entry.grid(row=1, column=1, sticky=(tk.W + tk.E))
        # hello_label.grid(row=0, column=0, columnspan=3)
        self.columnconfigure(1, weight=1)
