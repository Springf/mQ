import tkinter as tk
from tkinter import ttk
from mView import mView
from ctypes import windll
import mG_p4


class MyApplication(tk.Tk):
    """Hell Training Main Application"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        windll.shcore.SetProcessDpiAwareness(1)
        self.title("Math Fun")
        self.geometry("2048x1536")
        self.resizable(width=False, height=False)
        mv = mView(self)
        mv.grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.columnconfigure(0, weight=1)
        mv.grid(2, 2)

    def generate_timer(self, initial_timer_seconds: int):
        hh = initial_timer_seconds / 3600
        mm = initial_timer_seconds / 60 - hh
        ss = initial_timer_seconds % 3600 % 60

        return f'{str(hh).zfill(2)}:{str(mm).zfill(2)}:{str(ss).zfill(2)}'


if __name__ == '__main__':
    while True:
        mG_p4.pick()
    app = MyApplication()
    app.mainloop()
