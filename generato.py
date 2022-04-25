# here we are going to produce an arithmentic progression where the first term, the common difference and the number
#of terms entered by the user

from numpy import square


def arithmetic_progression(a,d,n):
    i=1
    while i<=n:
        yield (a+(i-1)*d)
        i+=1


a= int(input('enter the first term of the arithmetic progression \t :'))
d=int(input('enter the common difference of the arithmetic progression \t :'))
n=int(input('enter the number of terms of the arithmetic progression\t :'))
ap=arithmetic_progression(a,d,n)
print(ap)
for i in ap:
    print(i)

def geometric_progression(b,e,m):
    g=1;
    while g<=m:
        yield(b*pow(b,g-1))
        g+=1
b=int(input('enter the first term of the geometric progression \t :'))
c=int(input('enter the common ratio of the geometric progression \t :'))
m=int(input('enter the number of terms in the geometric progression \t :'))

gp=geometric_progression(b,c,m)
for g in gp:
    print(g)


# so can we do a fibonnacci sequence
def demo():
    print('start')
    for y in range (20):
        print('value of y before yeild \t:',y)
        yield y
        print('value of y after yield \t:',y)

    print('end')

p=demo()
for y in p:
    print(y)


