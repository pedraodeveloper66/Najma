"""Make a program that reads something on the keyboard and shows on the screen its primitive type and all possible information about it
"""
s = input('Type something: ')

print('O tipo primitivo desse valor é {}'.format(type(s)))
print('\nSó tem espaços? {}'.format(s.isspace()))
print('\nÉ um número? {}'.format(s.isnumeric()))
print('\nÉ alfabético? {}'.format(s.isalpha()))
print('\nÉ alfanumérico? {}'.format(s.isalnum()))
print('\nEstá em maiúsculas? {}'.format(s.isupper()))
print('\nEstá em minúsculas? {}'.format(s.islower()))
print('\nEstá capitalizada? {}'.format(s.istitle()))

