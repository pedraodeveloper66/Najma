"""
Make a program that reads the width and height of a wall in meters, calculate its area and the amount of paint needed to paint it, knowing that each liter of paint, paints an area of 2m².
"""

wallWidth = float(input('Largura da parede: '))

wallHeight = float(input('Altura da parede: '))

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(wallWidth, wallHeight, wallWidth *  wallHeight) + '\nPara pintar essa parede, você precisará de {} litros de tinta.'.format(wallWidth * wallHeight / 2))


