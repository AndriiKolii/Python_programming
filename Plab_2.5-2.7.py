# task 2.5
string = 'Andrii IKM-221д 122'
mylist = string.split(' ')

print(mylist[1])
print(string.replace('Andrii', 'Kolii'))
print(len(mylist), '\n')

# task 2.6
list1 = ['A', 'B', 'C', 'D', 'E']
list2 = ['a', 'b', 'c', 'd', 'e']
dictionary = {}

for i in range(0, 5):
    dictionary[list1[i]] = list2[i]

print(dictionary)

# task 2.7
a = set('ABCDE')
b = set('abcde')

a.add('W')
b.remove('e')
print(f'\nAdd: {a}\nRem: {b}')

if 'W' in a:
    print('"W" present in set')
else:
    print('Nope')
