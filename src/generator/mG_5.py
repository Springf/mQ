from decimal import Decimal
from entity.question import question
from random import randint, random
from fractions import Fraction

# collection of arithmatic questions for Primary 5

operators = ('+','-','*','/')
picker = ('gen_rand_equation',)
level = 5

def pick():
    p = randint(0, len(picker)-1)
    return globals()[picker[p]](5)


def gen_rand_decimal(whole, precision):
    min = 10 ** (whole + precision-1)
    max = 10 ** (whole + precision)
    p = 10 ** precision
    return Decimal(randint(min, max))/p

def gen_rand_int(whole):
    min = 10 ** (whole)
    max = 10 ** (whole + 1)
    return randint(min+1, max+1)

def recur_gen_rand_equation(p):
    if p == 1:
        return f'{gen_rand_int(1)}'
    operator = operators[randint(0,3)]
    if operator == '+':
        n1 = gen_rand_int(1)
        n2 = recur_gen_rand_equation(p-1)
        return f'{n2}+{n1}'
    elif operator == '-':
        n1 = gen_rand_int(0)
        s = recur_gen_rand_equation(p-1)
        n2 = eval(s)
        if n1 == n2:
            n1 = n1 + 11
        elif n1 < n2:
            return f'{s}-{n1}'   
        return f'{n1}-{s}'
    elif operator == '*':
        n1 = gen_rand_int(0)
        n2 = recur_gen_rand_equation(p-1)
        if p>2:
            return f'{n1}*({n2})'
        return f'{n2}*{n1}'
    elif operator == '/':
        ans = gen_rand_decimal(1,1)
        n1 = recur_gen_rand_equation(p-1)
        n1v = round(eval(n1),8)
        n2 = Decimal(f"{n1v}") * ans
        if p>2:
            return f'{n2}/({n1})'
        return f'{n2}/{n1}'

def gen_rand_equation(p):
    eq = recur_gen_rand_equation(p)
    ans = round(eval(eq),8)
    ans_in_decimal = Decimal(f'{ans}')
    q = question(None, f'{eq}=', f'{ans_in_decimal}', 'decimal', 5, 'Express your answer in Decimal')
    return q
    

