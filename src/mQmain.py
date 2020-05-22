import tkinter as tk
from tkinter import ttk
from mView import mView
from ctypes import windll
from entity.test import test
import getpass

class MyApplication(tk.Tk):
    """Hell Training Main Application"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        windll.shcore.SetProcessDpiAwareness(1)
        
        self.title("Math is Fun")
        self.geometry("1024x1024")
        #self.resizable(width=False, height=False)
            
        new_test = test(getpass.getuser(), 4, 30, 1200)
        mv = mView(self, new_test)

        #mv.grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.columnconfigure(0, weight=1)
        mv.grid(row=0, column=0, sticky=(tk.E + tk.W + tk.N + tk.S))


if __name__ == '__main__':
    # while True:
    #     mG_p4.pick()
    app = MyApplication()
    app.mainloop()
