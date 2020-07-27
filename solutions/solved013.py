"""
Make an algorithm that reads an employee's salary and shows his new salary, with a 15% increase.
"""

salary = float(input('Qual é o salário do Funcionário? R$'))

print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}'.format(salary, salary * 1.15))
    
    
