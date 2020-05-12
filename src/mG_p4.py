import random

def decimalAdd():
    n1 = round(random.random() * 101, 3)
    n2 = round(random.random() * 101, 2)
    ans = input(f'{n1} + {n2} = ')
    print(float(ans) == n1 + n2)