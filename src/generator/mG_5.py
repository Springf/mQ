from decimal import Decimal
from entity.question import question
from random import randint, random
from fractions import Fraction

# collection of arithmatic questions for Primary 5

operators = ('+','-','*','/')
picker = ('gen_rand_equation')
level = 5

def pick():
    return gen_rand_equation(5)
    # p = randint(0, len(picker)-1)
    # return globals()[picker[p]](4)


def gen_rand_decimal(whole, precision):
    min = 10 ** (whole + precision-1)
    max = 10 ** (whole + precision)
    p = 10 ** precision
    return Decimal(randint(min, max))/p

def gen_rand_int(whole):
    min = 10 ** (whole)
    max = 10 ** (whole + 1)
    return randint(min+1, max+1)

# def gen_rand_pair(operator)
#     x = gen_rand_int(2)
#     y = gen_rand_int(1)
#     return f'{x}{operator}{y}'


# def gen_rand_pair_wp(operator)
#     return f'({gen_rand_pair()})'

def recur_gen_rand_equation(p):
    if p == 1:
        return f'{gen_rand_int(1)}'
    operator = operators[randint(0,3)]
    if operator == '+':
        n1 = gen_rand_int(1)
        n2 = recur_gen_rand_equation(p-1)
        return f'{n1}+{n2}'
    elif operator == '-':
        n1 = gen_rand_int(0)
        n2 = eval(recur_gen_rand_equation(p-1))
        if n1 < n2:
            tmp = n1
            n1 = n2
            n2 = tmp
        return f'{n1}-{n2}'
    elif operator == '*':
        n1 = gen_rand_int(0)
        n2 = recur_gen_rand_equation(p-1)
        if p>2:
            return f'{n1}*({n2})'
        return f'{n1}*{n2}'
    elif operator == '/':
        ans = gen_rand_int(0)
        n1 = recur_gen_rand_equation(p-1)
        n2 = eval(f'{n1}') * ans
        if p>2:
            return f'{n2}/({n1})'
        return f'{n2}/{n1}'

def gen_rand_equation(p):
    eq = recur_gen_rand_equation(p)
    ans = eval(eq)
    q = question(None, f'{eq}=', f'{ans}', 'decimal', 5, 'Express your answer in Number')
    return q
    
def add_minus(np):
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
