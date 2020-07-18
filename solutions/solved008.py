"""
Write a program that reads a value in meters and displays it converted to centimeters and millimeters
"""
m = float(input('Uma distância em metros: '))

"""Kilometre --> Divide the length value by 1000"""
km = m / 1000
"""Hectometre --> Divide the length value by 100"""
hm = m / 100
"""Decametre --> Divide the length value by 10"""
dam = m / 10
"""Decimetre --> Multiply the length value by 10"""
dm = m * 10
"""Centimetre --> Multiply the length value by 100"""
cm = m * 100
"""Millimetre --> Multiply the length value by 1000"""
mm = m * 1000

print('A medida de {}m corresponde a\n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(m, km, hm, dam, dm, cm, mm))
