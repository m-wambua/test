# using the ternary operator

a= int(input('enter the first number\t :'))
b=int(input('enter the second number\t:'))
c=int(input('enter the third number \t :'))
great=(a if(a>c) else c)if (a>b) else (b if (b>c)else c)
print('the greatest of the three numbers is : ' +str(great))