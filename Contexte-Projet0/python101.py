import sys
import copy
print('Version', sys.version)

# Bonnes Pratiques
#
# CALTAL : Code a Little, Test a Little
# DRY: Don't Repeat Yourself
# UMUD: You Must Use the Debugger
# ...

# Norme de codage
#
# Python PEP 8
# PascalCase: types (classes, ...)
# lower_snake_case : fonctions, méthode, variable, ...
# UPPER_SNAKE_CASE : constantes, ...
# ...
# Lignes de 80 caractères (exclue de la norme)
# ...
# Nom de variable et types pertinent même s'ils sont longs
# Autodocumentation
#
# Pas de commentaires creux!!!
#

# Types de données fondamentaux
#
a = 3 # integer = IMMUTABLE
b = 3.14159265 # float = IMMUTABLE
c = 1+2j # complexe = IMMUTABLE
d = "Allo" # string = IMMUTABLE
e = True # boolean = IMMUTABLE
f = None # NoneType = IMMUTABLE
g = b'allo' # bytes = IMMUTABLE
h = bytearray(b'allo') # bytes = MUTABLE

# operateur ternaire
#
value = 5
print(value > 0 and value < 10)
print(0 < value < 10)

print('positif' if value >= 0 else 'negatif')

                                        # mutable | subscritable(read/write) | iterable  |  duplicate   |                       
my_str = 'string'                       # 0       | 1/0                      | 1         | 1            |                        
my_list = [0, 1 , 2, 3, 4]              # 1       | 1/1                      | 1         | 1            |                       
my_tuple = [0, 1, 2, 3, 4]              # 0       | 1/0                      | 1         | 1            |                       
my_set = {0, 1, 2}                      # 1       | 0/0                      | 1         | 1            |                       
my_dict = {0:'zero', 1:'un', 2:'deux'}  # 1       | 1/1                      | 1         | 0:1          |


# indexation et slicing
#
my_list = [10, 11, 12, 13, 14, 25, 26, 27, 28, 29]
print(my_list)
print(my_list[0]) # de gauche à droite de 0 à n-1
print(my_list[3])
print(my_list[9])
print(my_list[-1]) # droite à gauce de 1 à n 
print(my_list[-2]) 
print(my_list[0:3]) # de n à n, le 2eme index exclue
print(my_list[1:-2])
print(my_list[:])
print(my_list[:3])
print(my_list[-3:])
print(my_list[0:5:2])
print(my_list[8:3:-1])
print(my_list[::-1])

# iterator - conceptuellement
# i = my_list.iterator()        <<< implicite
# while i != my_list.iterator()     <<< imlicitement substitué par la ...
#       print(i) # do something     <<< corps de la boucle
#       i += 1                      <<< implicite

for i in my_list:
    print(i, end=' ')
print('')

for i in range(10):
        print(i, end=' ')
print('')
for i in range(3):
    print(i, end=' ')
print('')
for key in my_dict:
    print(key, end=' ')
print('')
for value in my_dict:
    print(value, end=' ')
print('')
for key, value in my_dict.items():
    print(key, ' => ', value)
    
# for i in range(len(my_dict)):
#     print (my_dict.key[i], ' => ', my_dict.values[i])

list_1 = ['a', 'l', 'l', 'o']
list_2 = [5, 12, 25, 7]
list_3 = [[1, 3], [2, 4], [5, 6]]

for i, value in enumerate(list_1):
    print('position', i, ' => ', value, ' ', ord(value))

for v1, v2 in zip(list_1, list_2):
    print(v1, ' <=> ', v2)

for v1, v2 in zip(list_1, list_2):
    v1 = 0
    print(v1)
    
    

# Compression Lists
# basic empty list construction

my_list = [] # 1
my_list = list() # 2

# basic list construction
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # 1
my_list = list(range(10)) # 2
my_list = [] # 3
for i in range(10):
    if i % 2:                       # |
            my_list.append(i)       # |
my_list = [None] * 10 # 4

# comprehension list
# my_list = [_expression)_for_member_in_iterable_ {if condition} ]
#
#
#

print('comprehension list')
my_list = []
for i in range(10):
    if i % 2:
        my_list.append(i**2)
print(my_list)

my_list = [i**2 for i in range(10) if i % 2]
my_list = [0 for _ in range(10)]



# Référence/Pointeur/'Garbage Collector
a = 3
print(a, hex(id(a)))
a = 4
print(a, hex(id(a)))
a = a**2
print(a, hex(id(a)))
a = 'allo'
print(a, hex(id(a)))
a = a*2
print(a, hex(id(a)))
a = [0, 1, 2, 3]
print(a, hex(id(a)))
a = [10, 11, 12, 13]
print(a, hex(id(a)))
a[0] = 200
print(a, hex(id(a)))
a[:] = [20, 21, 22, 23]
print(a, hex(id(a)))

b = a # Shallow copy
c = a[:] # Deep Copy
d = copy.deepcopy(a) #Deep Copy
print(b, hex(id(b)))
b[0] = 'cool'
print(b, hex(id(b)))
print(a, hex(id(a)))
print(c, hex(id(c)))
print(d, hex(id(d)))




a = (0, 'allo', (0, 1), [5, 'Cool'])
print(a[0])
a[3][0] = 'Hooo Yeah'
a[3].append('C52')
print(a[3])

