import math as mt

# task_1.1
a1 = 22
a2 = 0.314

print(f'ІКМ-221д, Колій Андрій')
print(f'a1: {a1}, {type(a1)} \na2: {a2}, {type(a2)}\n')

# task_1.2
x = float(input('First number: '))
y = float(input('Second number: '))

print(f'\nSum: {round(x+y,3)} \nDif: {round(x-y,3)} \nMul: {round(x*y,3)} \nDiv: {round(x/y,3)} '
      f'\n% {round(x%y,3)}\n')

# task_1.3
n = int(input('People: '))
m = float(input('Sum: '))

print(f'Individual fee: {round(m*1.15/n,3)}\n')

# task_1.4 var7
g = float(input('Numero: '))
p1 = mt.exp(0.6 * g - 1) - mt.sqrt(mt.pow(g + 6.1, 3))
p2 = mt.log(g) + mt.pow(mt.tan(g), 2)
print(f'Result: {round(mt.atan(g) + p1 / p2, 3)}')
