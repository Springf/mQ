import tkinter as tk
from tkinter import ttk
import threading
import config
import sqlite3
from entity.test import test

class mView(tk.Frame):
    """A friendly little module"""

    def __init__(self, parent, test):
        super().__init__(parent)
        self.root = parent
        self.root.protocol("WM_DELETE_WINDOW", self.close) 
        self.conn = sqlite3.connect(config.DATABASE_CONFIG['dbname'])
        self.test = test
        self.test.save_test(self.conn)
        self.test.generate_test(self.conn)
        self.current_question = 0

        self.question = self.test.list_of_questions[self.current_question]
        self.config_form()
        self.render_form()
        
    def update_answer(self):
        time_spent = self.last_time-self.time
        answer = self.answer.get()
        correct = answer == self.question.answer
        self.test.update_test_question(self.conn, self.question.id, answer, correct, time_spent)

    def next(self):
        self.update_answer()
        self.current_question = self.current_question + 1
        self.question = self.test.list_of_questions[self.current_question]
        if self.current_question == self.test.num_of_questions-1:
            self.button_next.config(text="Submit", command=self.submit)
        self.render_form()
    
    def submit(self):
        self.update_answer()
        self.test

    
    def config_form(self):
        self.question_body_frame = tk.LabelFrame(self, font=("Calibri", 32))
        self.question_body = tk.StringVar()
        question_body_label = tk.Label(self.question_body_frame, textvariable=self.question_body, font=(
            "Calibri", 48), wraplength=800)
        self.answer_frame = tk.LabelFrame(self, font=("Calibri", 32))
        self.answer = tk.StringVar()
        answer_entry = tk.Entry(self.answer_frame, textvariable=self.answer, font=("Calibri", 32))

        self.timer_text = tk.StringVar()
        self.time = self.test.time_limit
        self.last_time = self.time
        self.timer_text.set(self.generate_timer(self.time))
        
        timer_label = tk.Label(self, textvariable=self.timer_text, font=("Calibri", 32))

        self.button_next = tk.Button(self, text='Next', command=self.next, font=("Calibri", 32))

        self.question_body_frame.grid(row=0, columnspan=2, sticky=(tk.W + tk.E), padx=50)
        question_body_label.grid(row=0, sticky=(tk.W + tk.E),padx=50,pady=20)
        self.answer_frame.grid(row=1, columnspan=2, sticky=(tk.W + tk.E), padx=50)
        answer_entry.grid(row=1,sticky=(tk.W + tk.E), padx=100, pady=20)
        timer_label.grid(row=2, column=0, sticky=(tk.W + tk.S), padx=100, pady=50)
        self.button_next.grid(row=2, column=1,sticky=(tk.E+tk.S), padx=100,pady=50)
        self.columnconfigure(1, weight=1)

        self.timer = threading.Timer(1, self.reduce_time)
        self.timer.start()

    def render_form(self):
        self.question_body_frame.config(text=f'Question {self.current_question+1}')
        self.question_body.set(self.question.get_body())
       
        self.answer_frame.config(text=self.question.prompt)
        
        self.answer.set('')

        self.test.start_test_question(self.conn, self.question.id)

    def reduce_time(self):
        self.time = self.time-1
        if self.time == 0:
            self.submit()
        else:
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
        self.conn.commit()
        self.conn.close()
        self.root.destroy()