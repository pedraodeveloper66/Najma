"""
Create an algorithm that reads a number and shows its double, triple and square root.
"""
n = int(input('Digite um número: '))
print('O doblo de {} vale {}.\nO triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}.'.format(n, n*2, n, n*3, n, float(n**0.5)))
