import math
from decimal import Decimal
Decimal('.23') + Decimal('.42')
print(Decimal('.23') + Decimal('.42'))  
#  Decimal Context Mangager

#  Fractions
from fractions import Fraction
a = Fraction(5, 4)
b = Fraction(7, 16)
print(a + b)  # 27/16
print(float(a + b))  # 1.6875