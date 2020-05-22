from decimal import Decimal
from entity.question import question
from random import randint, random
from fractions import Fraction

# collection of arithmatic questions for Primary 4

picker = ('decimal_add', 'decimal_minus', 'decimal_multiply',
          'decimal_divide', 'faction_add', 'faction_minus')
level = 4

def pick():
    p = randint(0, len(picker)-1)
    return globals()[picker[p]]()


def gen_rand_decimal(whole, precision):
    min = 10 ** (whole + precision-1)
    max = 10 ** (whole + precision)
    p = 10 ** precision
    return Decimal(randint(min, max))/p


def decimal_add():
    n1 = gen_rand_decimal(2, 2)
    n2 = gen_rand_decimal(3, 1)
    ans = n1 + n2
    q = question(None, f'{n1} + {n2} =', f'{ans}', 'decimal', level, 'Express your answer in Decimal')
    return q


def decimal_minus():
    n1 = gen_rand_decimal(3, 2)
    n2 = gen_rand_decimal(3, 1)
    if n1 < n2:
        tmp = n1
        n1 = n2
        n2 = tmp
    ans = n1 - n2
    q = question(None, f'{n1} - {n2} =', f'{ans}', 'decimal', level, 'Express your answer in Decimal')
    return q


def decimal_multiply():
    n1 = gen_rand_decimal(1, 2)
    n2 = gen_rand_decimal(1, 1)
    ans = n1 * n2
    q = question(None, f'{n1} * {n2} =', f'{ans}', 'decimal', level, 'Express your answer in Decimal')
    return q


def decimal_divide():
    ans = gen_rand_decimal(3, 2)
    n1 = randint(2, 12)
    n2 = n1 * ans
    q = question(None, f'{n2} ÷ {n1} =', f'{ans}', 'decimal', level, 'Express your answer in Decimal')
    return q


def faction_add():
    n1 = Fraction(randint(1, 9), randint(9, 15))
    n2 = Fraction(randint(2, 9), randint(9, 16))
    ans = n1 + n2
    q = question(None, f'{n1} + {n2} =', f'{ans}', 'fraction', level, 'Express your answer in Simplified Fraction')
    return q

def faction_minus():
    n1 = Fraction(randint(1, 9), randint(9, 12))
    n2 = Fraction(randint(2, 9), randint(9, 16))
    if n1 < n2:
        tmp = n1
        n1 = n2
        n2 = tmp
    ans = n1 - n2
    q = question(None, f'{n1} - {n2} =', f'{ans}', 'fraction', level, 'Express your answer in Simplified Fraction')
    return q
