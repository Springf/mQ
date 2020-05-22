from decimal import Decimal
from entity.question import question
from random import randint, random

# collection of arithmatic questions for Primary 4

picker = ('integer_add', 'integer_minus', 'integer_multiply',
          'integer_divide')
level = 3

def pick():
    p = randint(0, len(picker)-1)
    return globals()[picker[p]]()


def gen_rand_int(whole):
    min = 10 ** (whole)
    max = 10 ** (whole + 1)

    return randint(min, max)


def integer_add():
    n1 = gen_rand_int(randint(1,5))
    n2 = gen_rand_int(randint(1,4))
    ans = n1 + n2
    q = question(None, f'{n1} + {n2} =', f'{ans}', 'int', level, 'Express your answer in number')
    return q


def integer_minus():
    n1 = gen_rand_int(randint(1,5))
    n2 = gen_rand_int(randint(1,5))
    if n1 < n2:
        tmp = n1
        n1 = n2
        n2 = tmp
    ans = n1 - n2
    q = question(None, f'{n1} - {n2} =', f'{ans}', 'int', level, 'Express your answer in number')
    return q


def integer_multiply():
    n1 = gen_rand_int(randint(1,3))
    n2 = gen_rand_int(randint(1,2))
    ans = n1 * n2
    q = question(None, f'{n1} * {n2} =', f'{ans}', 'int', level, 'Express your answer in number')
    return q


def integer_divide():
    ans = gen_rand_int(randint(1,3))
    n1 = randint(2, 12)
    n2 = n1 * ans
    q = question(None, f'{n2} ÷ {n1} =', f'{ans}', 'int', level, 'Express your answer in number')
    return q
