import config
import sys
sys.path.insert(1, '../')
from entity.question import question

db = config.DATABASE_CONFIG['dbname']

def test_insert_data():
    q = question(db, None, "1+2", 3, "number", 1, "=")
    assert q.get_body() == '1+2'
    assert hasattr(q, 'variable_id') == False
    assert q.variable is None
    assert q.answer == 3
    assert q.answer_type == 'number'
    assert q.level == 1
    q.update()
