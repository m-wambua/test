## we start on loops!!!

#first we will start with the while loop and doing so using it to calculate the factorial of a number

from math import factorial


n= input('enter the number in which you want to get its factorial: ')
m = int(n)
factorial=1
i=1
while i<=m:
    factorial=factorial*i
    i=i+1

print('\ the factorial of the number:  ' +str(m)+ '  you wish to establish is:  ' +str(factorial))


## say we want to use the while loop to get the power of a number

a=int(input('enter the first number'))
b=int(input('enter the second number'))
print(' so our function at this point is to create "a" which is '+str(a)+' power "b" which is '+str(b))

power=1
i=1
while i<= b:
    power = power*a
    i=i+1

else:
    print(str(a)+ ' to the power of '+str(b)+' is '+str(power))

## getting the arithmetic progression can also be obtained

c=int(input('enter the first term of the arithmetic progression  :\t'))
d=int(input('enter the common difference  :\t'))
e=int(input('enter the number of terms  :\t'))
t=1
sum=0
while t<=e:
    term = a+(t-1)*d
    print('the '+str(t)+ ' th term is '+str(term))
    sum=sum+term
    t=t+1

else:
    print('the sum of '+str(t)+ ' terms is\t:'+str(sum))

## next one would be the geometric progression

f=int(input('enter the first term of the geometric progression\t :'))
g=int(input('enter the common ratio\t: '))
h=int(input('enter the number of terms\t:'))
v=1
sum_1=0

while v<=h:
    term = f*(g**v-1)
    print('the '+str(v)+'th term is'+str(term))
    sum_1=sum_1+term
    v=v+1

else:
    print('the sum of'+str(h)+'terms is\t:'+str(sum))


