# the fibonacci sequence aka the rabbit problem

def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return(fib(n-1)+fib(n-2))

n=int(input('enter the nth element : \t'))
f=fib(n)
print('the nth fibonacci is\t  :'+str(f))
## technically in used a global variable for the two functions

def fac(n):
    if n==1:
        return 1

    else:
        return(n*fac(n-1))

fc=fac(n)
print('the factorial of the number is also \t :  '+str(fc))

## one can also use recursion to find the nth power of a number

def power(a,b):
    if b==1:
        return a
    else:
        return(a*power(a,b-1))
a=int(input('enter the first number \t :'))
b=int(input('enter the second number \t :'))
p=power(a,b)
print(a,' to the power ',b,'is',p)
