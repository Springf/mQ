import sqlite3

class question:
    """
    A question has a body, an answer, a difficulty level and a prompt;
    optionally it can has the variables in the body, the actual value in args
    """
    def __init__(self, db, id, body, answer, answer_type, level, prompt, variable=None, variable_id=None):
        self.db = db
        self.id = id
        self.body = body
        self.answer = answer
        self.answer_type = answer_type
        self.level = level
        self.prompt = prompt
        if variable is not None:
            self.variable = variable.split(',')
            self.variable_id = variable_id
        else:
            self.variable = None
    def __init__(self, db, id):
        

    def populate(self):
        if self.id is not None:
            selct_sql = f"""SELECT q.id, q.body, q.answer, q.answer_type, q.level, q.prompt
            ,v.variable, v.variable_id 
            FROM question q LEFT JOIN variable v ON q.id = v.question_id
            """
            conn = sqlite3.Connection(self.db)
            cur = conn.cursor()
            cur.execute(insert_sql)

    def get_body(self):
        if self.variable is not None:
            return self.body.format(*self.variable)
        return self.body

    def update(self):
        if self.id is None:
            insert_sql = f"""INSERT INTO question (body, answer, answer_type, level, prompt, created_datetime)
                VALUES ('{self.body}', '{self.answer}', '{self.answer_type}', {self.level}, '{self.prompt}',datetime('now', 'localtime'))
                """
            id_sql = 'select last_insert_rowid()'
            conn = sqlite3.Connection(self.db)
            cur = conn.cursor()
            cur.execute(insert_sql)
            new_id = cur.execute(id_sql).fetchone()
            if self.variable is not None and self.variable_id is None:
                insert_variable_sql = f"""INSERT INTO variable (question_id, variable, created_datetime)
                VALUES ({new_id}, {','.join(self.variable)},datetime('now', 'localtime'))
                """
                cur.execute(insert_variable_sql)
            conn.commit()
            conn.close()