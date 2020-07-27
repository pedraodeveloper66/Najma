"""
Write a program that asks how many kilometers a rental car has driven and how many days it has been rented. Calculate the price to pay, knowing that the car costs R$ 60 per day and R$ 0.15 per km driven.
"""

days = int(input('Quantos dias alugados? '))
kmDriven = float(input('Quantos Km rodados? '))

print('O total a pagar é de R${:.2f}'.format(days*60.00+kmDriven*0.15))
    

