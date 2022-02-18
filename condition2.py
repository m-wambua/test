## a program to find the greatest number entered by a user

print('please enter three number\t:')
num_a=int(input('your first number is : \t'))
print(num_a)
num_b=int(input('your second number is : \t'))
print(num_b)
num_c=int(input('your third number is :  \t'))
print(num_c)
if int(num_a)>int(num_b) :
    if int(num_a>int(num_c)):
        big=int(num_a)
else:# here it means num_b is already greater than num_a
    if int(num_b)>int(num_c):# so comparing it with num_c directly
        
        big=int(num_b)
    else:
        big=num_c

print(big)

