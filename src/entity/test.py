import question

"""
test will have:
an id
a list of questions
question marks
time limit
difficulty level
time started
time ended
the one who take the test
"""


class test:
    def __init__(self, taker, level, num_of_questions, time_limit):
        self.taker = taker
        self.level = level
        self.num_of_questions = num_of_questions
        self.time_limit = time_limit
