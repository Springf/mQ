from random import randint, random
from fractions import Fraction
import sys
sys.path.insert(1, '../')
from entity.question import question
import config

# collection of arithmatic questions for Primary 4

picker = ('decimalAdd', 'decimalMinus', 'decimalMultiply', 'decimalDivide', 'factionAdd')
db = config.DATABASE_CONFIG['dbname']
level = 4
def pick():
    print(len(picker))
    p = randint(0, len(picker)-1)
    globals()[picker[p]]()


def decimalAdd():
    n1 = round(random() * 101, 3)
    n2 = round(random() * 101, 2)
    ans = input(f'{n1} + {n2} = ')
    print(float(ans) == n1 + n2)
    print(n1+n2)


def decimalMinus():
    n1 = round(random() * 101, 3)
    n2 = round(random() * 101, 2)
    if n1 < n2:
        tmp = n1
        n1 = n2
        n2 = tmp
    ans = input(f'{n1} - {n2} = ')
    print(float(ans) == n1 - n2)
    print(n1-n2)


def decimalMultiply():
    n1 = round(random() * 101, 3)
    n2 = round(random() * 101, 2)
    ans = input(f'{n1:.3f} * {n2:.2f} = ')
    print(float(ans) == n1 * n2)
    print(n1*n2)


def decimalDivide():
    n1 = round(random() * 101, 3)
    n2 = randint(2, 12)
    n3 = n1 * n2
    ans = input(f'{n3:.3f} / {n2} = ')
    print(float(ans) == n1)
    print(n1)

def factionAdd():
    n1 = Fraction(randint(1,9), randint(9,20))
    n2 = Fraction(randint(1,9), randint(9,20))
    ans = n1 + n2
    q = question(db, None, f'{n1} + {n2}', f'{ans}','fraction',level,'=')
    #q.update()
    print(q.body)
    return q
