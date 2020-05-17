import sqlite3
from . import config
import pytest
from ..entity.test import test

db = config.DATABASE_CONFIG['dbname']


def test_new_test():
    t = test('fengchun', 4, 20, 600)
    assert t.num_of_questions == 20
    assert t.time_limit == 600
    assert t.level == 4


def test_new_test_save(db_connection):
    t = test('fengchun', 4, 20, 600)
    assert t.num_of_questions == 20
    assert t.time_limit == 600
    assert t.level == 4
    id = t.save_test(db_connection)
    assert id != 0
    cur = db_connection.cursor()
    cur.execute(
        f"""select level, taker, time_limit, created_datetime
        , start_datetime, end_datetime from test where id = {id}""")
    result = cur.fetchone()
    assert result is not None
    assert result[0] == 4
    assert result[1] == 'fengchun'
    assert result[2] == 600
    assert result[3] is not None
    assert result[4] is None
    assert result[5] is None

def test_new_test_gen_test(db_connection):
    t = test('fengchun', 4, 20, 600)
    assert t.num_of_questions == 20
    assert t.time_limit == 600
    assert t.level == 4
    id = t.save_test(db_connection)
    assert id != 0
    t.generate_test(db_connection)
    cur = db_connection.cursor()
    cur.execute(
        f"""select test_id, question_id, variable_id, [order]
        , mark, t.answer, correct
        , q.level, q.answer
        from test_questions t join question q on t.question_id = q.id 
        where test_id = {id} order by [order]""")
    result = cur.fetchall()
    print(result)
    assert result is not None
    assert len(result) == 20
    assert result[0][0] == id
    assert result[0][1] is not None
    assert result[0][2] is None
    assert result[0][3] == 0
    assert result[0][4] == 1
    assert result[0][5] is None
    assert result[0][6] is None
    assert result[0][7] == 4
    assert result[0][8] is not None

    assert result[19][0] == id
    assert result[19][1] is not None
    assert result[19][2] is None
    assert result[19][3] == 19
    assert result[19][4] == 1
    assert result[19][5] is None
    assert result[19][6] is None
    assert result[19][7] == 4
    assert result[19][8] is not None


@pytest.fixture(scope="module", autouse=True)
def db_connection():
    conn = sqlite3.connect(db)
    yield conn
    cur = conn.cursor()
    cur.execute("delete from question")
    cur.execute("delete from variable")
    cur.execute("delete from test")
    cur.execute("delete from test_questions")
    conn.commit()
    conn.close()
