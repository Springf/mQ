from .question import question
from generator import *
from random import randint
import sqlite3

"""
test will have:
an id
a list of questions
question marks
time limit in seconds
difficulty level
time started
time ended
the one who take the test
"""


class test:
    test_generators = ('mG_1', 'mG_2', 'mG_4', 'mG_4', 'mG_4')

    def __init__(self, db, taker, level, num_of_questions, time_limit):
        self.taker = taker
        self.level = level
        self.num_of_questions = num_of_questions
        self.time_limit = time_limit
        self.db = db

    def save_test(self):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.execute(f"""INSERT INTO test (level, taker, time_limit, created_datetime)
                        VALUES ({self.level}, '{self.taker}', {self.time_limit}, datetime('now','localtime'))
                    """)
        id_sql = 'select last_insert_rowid()'
        new_id = cur.execute(id_sql).fetchone()[0]
        conn.commit()
        conn.close()
        self.id = new_id
        return new_id

    def save_test_question(self, question_id, order, mark):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.execute(f"""INSERT INTO test_questions (test_id, question_id, order, mark)
                        VALUES ({self.id}, {question_id}, {order}, {mark})
                    """)
        conn.commit()
        conn.close()

    def generate_test(self):
        self.list_of_quetions = dict()
        for i in range(0, self.num_of_questions):
            # calculate mark based on level - TODO
            mark = 1
            pick_a_question(randint(self.level - 2, self.level))
            question_id = q.update()
            self.list_of_quetions[i] = q
            save_test_question(question_id, i, mark)

    def pick_a_question(self, level):
        rand_gen = self.test_generators[level]
        gen = importlib.import_module(rand_gen)
        q = gen.pick(self.db)
        return q.update()
