"""
Make an algorithm that reads the price of a product and shows its new price, with 5% discount.
"""

price = float(input('Qual é o preço do produto? R$'))

print('O produto que custava R${}, na promoção com desconto de 5% vai custa R${:.2f}'.format(price, 0.95 * price))
    
    
