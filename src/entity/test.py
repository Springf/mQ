from question import question
from generator import *
from random import randint
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

    def __init__(self, taker, level, num_of_questions, time_limit):
        self.taker = taker
        self.level = level
        self.num_of_questions = num_of_questions
        self.time_limit = time_limit

    def generate_test(self, db):
        rand_gen = self.test_generators[randint(self.level-2, self.level)]
        gen = importlib.import_module(rand_gen)
        q = gen.pick()
        q = question(db, None, )
