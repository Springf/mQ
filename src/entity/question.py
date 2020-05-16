import config
import sqlite3

class question:
    """
    A question has a body, an answer, a difficulty level and a prompt;
    optionally it can has the variables in the body, the actual value in args
    """
    def __init__(self, body, answer, answer_type, level, prompt, variable=None, variable_id=None):
        self.id = id
        self.body = body
        self.answer = answer
        self.answer_type = answer_type
        self.level = level
        self.prompt = prompt
        if variable is not None:
            self.variable = variable.split(',')
            self.variable_id = variable_id

    def get_body(self):
        return body.format(*variable)

    def update(self):
        if self.id is None:
            insert_sql = f"""INSERT INTO question (body, answer, answer_type, level, prompt)
                VALUES ({body}, {answer}, {answer_type}, {level}, {prompt})
                """
            id_sql = 'select last_insert_rowid()'
            conn = sqlite3.Connection(config.DATABASE_CONFIG['dbname'])
            cur = conn.cursor()
            cur.execute(insert_sql)
            new_id = cur.execute(id_sql).fetchone()
            if self.variable is not None and self.variable_id is None:
                insert_variable_sql = f"""INSERT INTO variable (question_id, variable)
                VALUES ({new_id}, {','.join(self.variable)})
                """
                cur.execute(insert_variable_sql)
            conn.commit()
            conn.close()