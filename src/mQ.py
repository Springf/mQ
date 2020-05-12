import tkinter as tk
from tkinter import ttk
from mView import mView
from ctypes import windll


class MyApplication(tk.Tk):
    """Hello World Main Application"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        windll.shcore.SetProcessDpiAwareness(1)
        self.title("Math Fun")
        self.geometry("2048x1536")
        self.resizable(width=False, height=False)
        mv = mView(self)
        mv.grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.columnconfigure(0, weight=1)


if __name__ == '__main__':
    app = MyApplication()
    app.mainloop()
