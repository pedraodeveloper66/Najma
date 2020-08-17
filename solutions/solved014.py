"""
Write a program that converts a entered temperature to ° C and converts to ºF.
"""

temperature = float(input('Informe a temperatura em °C: '))

print('A temperatura de {:.1f}°C corresponde a {:.1f}°F'.format(temperature, temperature * 9 / 5 + 32))
