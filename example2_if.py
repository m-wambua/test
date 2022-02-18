# so the following program asks the user to enter the coefficient of two lines 
# and estimates if th lines are parallel or if they overlap or intersect
print('enter the coeffiecients of the first eqation [a1(x) +b1(y) + c1 = 0] \n')
r1=input('enter the value of a1: ')
a1=int(r1)
r1=input('enter the value of b1: ')
b1=int(r1)
r1=input('enter the value of c1: ')
c1=int(r1)

print('enter coefficients of the second equation[a2(x) + b2(y) + c2 =0]\n')
r2=input('enter the value of a2 : ')
a2= int(r2)
r2=input('enter the value of b2 : ')
b2=int(r2)
r2=input('enter the value of c2 : ')
c2= int(r2)

if ((a1/a2)==(b1/b2))&((a1/a2)==(c1/c2)):
    print('lines overlap')

elif (a1/a2)==(b1/b2):
    print('lines are parallel')
else:
    print('lines intersect')