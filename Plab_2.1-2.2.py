# task 2.1
x = int(input('x:'))
y = int(input('y:'))

if x > 0 and y > 0:
    print(f'Quarter: I')
elif x > 0 > y:
    print(f'Quarter: IV')
elif x < 0 < y:
    print(f'Quarter: II')
else:
    if x == y == 0:
        print(f'Origin')
    elif x == 0 or y == 0:
        print(f'Belongs to the axis')
    else:
        print(f'Quarter: III')

# task 2.2
x2 = float(input('\nX value:'))

if 0 <= x2 < 1:
    y2 = 0
elif x2 < 0:
    y2 = x2
else:
    y2 = 2 * x2
print(y2)
