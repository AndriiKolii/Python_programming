# task 2.3
while True:
    try:
        x3 = float(input('First number: '))
        y3 = float(input('Second number: '))
        break
    except ValueError:
        print('ValueError\n')


def summ(x, y):
    return x + y


def dif(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    return x / y


dic = {'+': summ, '-': dif, '*': mult, '/': div}

while True:
    try:
        opr = input('Operation: ')
        print(f'Result: {dic[opr](x3, y3)}')
        break
    except ZeroDivisionError:
        print('ZeroDivisionError\n')
