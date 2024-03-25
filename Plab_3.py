import random
import numpy as np
import datetime


# task_1
def var_7(txt):
    symbols = ['+', '-', '*', '/']
    if txt in symbols:
        print(f'True')
    else:
        print(f'You tried')


# task_4
def positive_counter(lst):
    n = len(lst)
    first, second = 0, 0
    half = n / 2
    if n % 2 != 0:
        half = int(np.ceil(n / 2))
    for i in range(half):
        if lst[i] > 0:
            first += 1
    for i in range(half, n):
        if lst[i] > 0:
            second += 1
    if first > second:
        print(f'In 1-st half')
    elif first == second:
        print(f'Tie')
    else:
        print(f'In 2-nd half')

    return first, second


# task_5
def tickets():
    tick = [0, 0, 0]
    tick[0] = int(input('A: '))
    tick[1] = int(input('B: '))
    tick[2] = int(input('C: '))
    return tick


def revenue():
    array = tickets()
    price = [10, 20, 50]
    money = [0] * len(array)
    for i in range(len(array)):
        money[i] = array[i] * price[i]
    print(f'Total income: {sum(money)}')
    return money


# task_6
def rectime(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        bone = datetime.datetime.now() - start
        print(f'Run time: {bone} seconds')
    return wrapper


@rectime
def tuple_time():
    my_tuple = (random.randrange(-1000000, 1000000) for _ in range(1000000))
    return my_tuple


@rectime
def list_time():
    lst = [random.randrange(-1000000, 1000000) for _ in range(1000000)]
    return lst


if __name__ == '__main__':

    '''    
    text = input(f'Whatever:')
    var_7(text)

    # task_2
    numb = [random.randrange(0, 21) for _ in range(10)]
    double = list(map(lambda x: x * 2, numb))
    print(f'\nTask_2:\n{numb}\nNew: {double}')

    # task_3
    text = 'This is text. Nice to meet you. Do we really need exactly twenty words? Is it necessary? Well, guess so'
    sth = text.split()
    reg = ' '.join(map(lambda y: y.title(), sth))
    print(f'\nTask_3:\n{reg}')

    # task_4
    seq = [random.randrange(-3, 3) for _ in range(5)]
    print('\nTask 4')
    print(seq)
    print(positive_counter(seq))

    # task_5
    print('\nTask 5')
    print(revenue())'''

 # task_6
    tuple_time()
    list_time()
