select * from question q join test_questions tq on tq.question_id = q.id
where tq.test_id in (SELECT max(id) from test)