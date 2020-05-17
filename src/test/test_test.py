import sqlite3
import config
import pytest
import sys
sys.path.insert(1, '../')
from entity.test import test

db = config.DATABASE_CONFIG['dbname']


def test_new_test():
    t = test(db, 'fengchun', 4, 20, 600)
    assert t.num_of_questions == 20
    assert t.time_limit == 600
    assert t.level == 4


def test_new_test_save():
    t = test(db, 'fengchun', 4, 20, 600)
    assert t.num_of_questions == 20
    assert t.time_limit == 600
    assert t.level == 4
    id = t.save_test()
    assert id != 0
    conn = sqlite3.connect(db)
    cur = conn.cursor()
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


@pytest.fixture(scope="module", autouse=True)
def clean_up():
    yield
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("delete from question")
    cur.execute("delete from variable")
    cur.execute("delete from test")
    cur.execute("delete from test_questions")
    conn.commit()
    conn.close()
