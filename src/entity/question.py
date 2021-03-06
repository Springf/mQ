import sqlite3
from fractions import Fraction
from decimal import Decimal


class question:
    """
    A question has a body, an answer, a difficulty level and a prompt;
    optionally it can has the variables in the body, the actual value in args
    """

    def __init__(self, id, body, answer, answer_type, level, prompt, variable=None, variable_id=None):
        self.id = id
        self.body = body
        if answer_type == 'int':
            self.answer = int(answer)
        elif answer_type == 'float':
            self.answer = float(answer)
        elif answer_type == 'decimal':
            self.answer = Decimal(answer)
        elif answer_type == 'fraction':
            self.answer = Fraction(answer)
        else:
            self.answer = answer
        self.answer_type = answer_type
        self.level = level
        self.prompt = prompt
        if variable is not None:
            self.variable = variable.split(',')
            self.variable_id = variable_id
        else:
            self.variable = None

    def get_body(self):
        if self.variable is not None:
            return self.body.format(*self.variable)
            #todo optimize
        if self.answer_type != 'fraction':
            return self.body.replace('/', '÷')
        return self.body

    def test_answer(self, answer):
        try:
            if self.answer_type == 'int':
                return self.answer == int(answer)
            elif self.answer_type == 'float':
                return self.answer == float(answer)
            elif self.answer_type == 'decimal':
                return self.answer == Decimal(answer)
            elif self.answer_type == 'fraction':
                return self.answer == Fraction(answer)
            else:
                return self.answer == answer
        except:
            return 0


    def update(self, conn):
        if self.id is None:
            insert_sql = f"""INSERT INTO question (body, answer, answer_type, level, prompt, created_datetime)
                VALUES ('{self.body}', '{self.answer}', '{self.answer_type}', {self.level}, '{self.prompt}',datetime('now', 'localtime'))
                """
            id_sql = 'select last_insert_rowid()'
            cur = conn.cursor()
            cur.execute(insert_sql)
            new_id = cur.execute(id_sql).fetchone()[0]
            if self.variable is not None and self.variable_id is None:
                insert_variable_sql = f"""INSERT INTO variable (question_id, variable, created_datetime)
                VALUES ({new_id}, '{','.join(self.variable)}',datetime('now', 'localtime'))
                """
                cur.execute(insert_variable_sql)
            self.id = new_id
            return new_id

    @staticmethod
    def populate(conn, id):
        if id is not None:
            select_sql = f"""SELECT q.id, q.body, q.answer, q.answer_type, q.level, q.prompt
            ,v.variable, v.id as variable_id 
            FROM question q LEFT JOIN variable v ON q.id = v.question_id
            WHERE q.id = {id} 
            """
            print(select_sql)
            cur = conn.cursor()
            results = cur.execute(select_sql).fetchall()
            for r in results:
                yield question(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7])
