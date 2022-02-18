from cmath import sqrt


print(2+3)
print(2*3)
print(2**3)# this gives the power notation
print(2/3)
print(2%3)
print(3/2)

print(sqrt(-3))
print(2//5)

import math

print(math.ceil(3.254))# the nearest integeer greater than ir equal to that number
print(math.copysign(-3,4))# copy the sign  of the number to the right
x= -3.4
print(math.fabs(x))# returns the basolute value of the number keyed
print(math.factorial(34))# the factorial of thatv number


print(math.floor(4.72))# the opposite of ceiling

###fractions
from fractions import Fraction
print(Fraction(128,-26))
print(Fraction('2/5'))
from  decimal import Decimal
print(Fraction(Decimal('1.1')))
