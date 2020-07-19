"""
Make a program that reads any integer and shows your multiplication table on the screen.
"""

num = int(input('Digite um número para ver sua tabuada: '))

print('-' * 12)

print(5 * ' ' + 'TABUADA {}'.format(num) + ' ' *5)  

for i in range(10):
    print('{:2} x {} = {:2}\n'.format(i+1, num, num*(i+1)))

print('-' * 12)
    
