from .question import question
from random import randint
import sqlite3
import importlib

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
    test_generators = ('..generator,mG_1', '..generator.mG_2'
    , '..generator.mG_4', '..generator.mG_4', '..generator.mG_4')

    def __init__(self, taker, level, num_of_questions, time_limit):
        self.taker = taker
        self.level = level
        self.num_of_questions = num_of_questions
        self.time_limit = time_limit

    def save_test(self, conn):
        cur = conn.cursor()
        cur.execute(f"""INSERT INTO test (level, taker, time_limit, created_datetime)
                        VALUES ({self.level}, '{self.taker}', {self.time_limit}, datetime('now','localtime'))
                    """)
        id_sql = 'select last_insert_rowid()'
        new_id = cur.execute(id_sql).fetchone()[0]
        self.id = new_id
        return new_id

    def pick_a_question(self, level):
        rand_gen = self.test_generators[level]
        gen = importlib.import_module(rand_gen, package='mQ.src.generator')
        q = gen.pick()
        return q

    def generate_test(self, conn):
        self.list_of_quetions = dict()
        cur = conn.cursor()
        for i in range(0, self.num_of_questions):
            # calculate mark based on level - TODO
            mark = 1
            q = self.pick_a_question(randint(self.level - 2, self.level))
            q.update(conn)
            self.list_of_quetions[i] = q
            cur.execute(f"""INSERT INTO test_questions (test_id, question_id, [order], mark)
                        VALUES ({self.id}, {q.id}, {i}, {mark})
                    """)