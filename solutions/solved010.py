"""
Create a program that reads how much money a person has in their wallet and shows how many dollars they can buy.

Consider: US$ 1.00 = R$ 3,27
"""
CURRENCYINREAL = 3.27

money = float(input('Quanto dinheiro você tem na carteira? R$'))

print('Com R${:.2f} você pode comprar U$${:.2f}'.format(money,CURRENCYINREAL/money))
    
