from . import config
import sqlite3
from ..src.entity.question import question
import pytest

db = config.DATABASE_CONFIG['dbname']

def test_new_question_int():
    q = question(None, "1+2", 3, "int", 1, "=")
    assert q.get_body() == '1+2'
    assert hasattr(q, 'variable_id') == False
    assert q.variable is None
    assert q.answer == 3
    assert q.answer_type == 'int'
    assert q.level == 1

def test_new_question_int_str():
    q = question(None, "1+2", '3', "int", 1, "=")
    assert q.get_body() == '1+2'
    assert hasattr(q, 'variable_id') == False
    assert q.variable is None
    assert q.answer == 3
    assert q.answer_type == 'int'
    assert q.level == 1

def test_new_question_float():
    q = question(None, "1+2.1", 3.1, "float", 1, "=")
    assert q.get_body() == '1+2.1'
    assert hasattr(q, 'variable_id') == False
    assert q.variable is None
    assert q.answer == 3.1
    assert q.answer_type == 'float'
    assert q.level == 1

def test_new_question_float_str():
    q = question(None, "1+2.1", '3.1', "float", 1, "=")
    assert q.get_body() == '1+2.1'
    assert hasattr(q, 'variable_id') == False
    assert q.variable is None
    assert q.answer == 3.1
    assert q.answer_type == 'float'
    assert q.level == 1

def test_new_question_float_with_var():
    q = question(None, "{}+{}", '3.1', "float", 1, "=", "1,2.1")
    assert q.get_body() == '1+2.1'
    assert q.variable_id is None
    assert q.variable == ['1','2.1']
    assert q.answer == 3.1
    assert q.answer_type == 'float'
    assert q.level == 1

def test_load_question_int(db_connection):
    q = question(None, "1+2", 3, "int", 1, "=")
    id = q.update(db_connection)
    qs = list(question.populate(db_connection, id))
    assert len(qs) == 1
    q = qs[0]
    assert q.get_body() == '1+2'
    assert hasattr(q, 'variable_id') == False
    assert q.variable is None
    assert q.answer == 3
    assert q.answer_type == 'int'
    assert q.level == 1
    none_id = q.update(db_connection)
    assert none_id is None

def test_load_question_float_with_var(db_connection):
    q = question(None, "{}+{}", '3.1', "float", 1, "=", "1,2.1")
    id = q.update(db_connection)
    qs = list(question.populate(db_connection, id))
    assert len(qs) == 1
    q = qs[0]
    assert q.get_body() == '1+2.1'
    assert q.variable_id is not None
    assert q.variable == ['1','2.1']
    assert q.answer == 3.1
    assert q.answer_type == 'float'
    assert q.level == 1
    none_id = q.update(db_connection)
    assert none_id is None

@pytest.fixture(scope="module", autouse=True)
def db_connection():
    conn = sqlite3.connect(db)
    yield conn
    cur = conn.cursor()
    cur.execute("delete from question")
    cur.execute("delete from variable")
    conn.commit()
    conn.close()
