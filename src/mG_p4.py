from random import randint, random

# collection of decimal questions

picker = ('decimalAdd', 'decimalMinus', 'decimalMultiply', 'decimalDivide')


def pick():
    p = randint(0, 3)
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
    n2 = round(random() * 101, 0)
    ans = input(f'{n1} * {n2} = ')
    print(float(ans) == n1 * n2)
    print(n1*n2)


def decimalDivide():
    n1 = round(random() * 101, 3)
    n2 = randint(2, 12)
    n3 = n1 * n2
    ans = input(f'{n3} / {n2} = ')
    print(float(ans) == n1)
    print(n1)
