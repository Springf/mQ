import tkinter as tk
from tkinter import ttk
import threading

class mView(tk.Frame):
    """A friendly little module"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.root = parent
        self.root.protocol("WM_DELETE_WINDOW", self.close) 
        
        self.question_no = tk.StringVar()
        self.question_body = tk.StringVar()
        self.question_prompty = tk.StringVar()
        self.answer = tk.StringVar()
        self.timer_text = tk.StringVar()
        self.time = 1200
        self.timer_text.set(self.generate_timer(self.time))
        self.timer = threading.Timer(1, self.reduce_time)
        self.timer.start()
        
        self.question_prompty.set("Express your answer in decimal")
        self.question_no.set('Question 1')
        self.question_body.set("""23.546 * 12 = """)
        
        question_body_frame = tk.LabelFrame(self, text='Question 1', font=("Calibri", 32))
        question_body_label = tk.Label(question_body_frame, textvariable=self.question_body, font=(
            "Calibri", 48), wraplength=800)
        
        #question_prompt_label = ttk.Label(question_body_frame, textvariable=self.question_prompty, font=(
        #    "Calibri", 32))
        answer_frame = tk.LabelFrame(self, text=self.question_prompty.get(), font=("Calibri", 32))
        answer_entry = tk.Entry(answer_frame, textvariable=self.answer, font=("Calibri", 32))

        timer_label = tk.Label(self, textvariable=self.timer_text, font=("Calibri", 32))
        button_next = tk.Button(self, text='Next', command=self.next, font=("Calibri", 32))

        
        
        question_body_frame.grid(row=0, columnspan=2, sticky=(tk.W + tk.E), padx=50)
        question_body_label.grid(row=0, sticky=(tk.W + tk.E),padx=50,pady=20)
        #question_prompt_label.grid(row=1, sticky=(tk.W + tk.E), padx=100)
        answer_frame.grid(row=1, columnspan=2, sticky=(tk.W + tk.E), padx=50)
        answer_entry.grid(row=1,sticky=(tk.W + tk.E), padx=100, pady=20)
        timer_label.grid(row=2, column=0, sticky=(tk.W + tk.S), padx=100, pady=50)
        button_next.grid(row=2, column=1,sticky=(tk.E+tk.S), padx=100,pady=50)
        # name_label.grid(row=1, column=0, sticky=tk.W)
        # name_entry.grid(row=1, column=1, sticky=(tk.W + tk.E))
        # hello_label.grid(row=0, column=0, columnspan=3)
        self.columnconfigure(1, weight=1)

    def next(self):
        print("next clicked")

    def reduce_time(self):
        self.time = self.time-1
        self.timer_text.set(self.generate_timer(self.time))
        self.timer = threading.Timer(1, self.reduce_time)
        self.timer.start()

    def generate_timer(self, timer_seconds: int):
        hh = timer_seconds // 3600
        mm = timer_seconds // 60 - hh
        ss = timer_seconds % 3600 % 60

        return f'{str(hh).zfill(2)}:{str(mm).zfill(2)}:{str(ss).zfill(2)}'

    def close(self):
        self.timer.cancel()
        self.root.destroy()