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


# another way of doing the generator function is

L1=[x**3 for x in range (10)]
print(L1)
L2=[3**x for x in range (2,10,1)]#means move from 2 to 10 with increaments of 1
print(L2)
L3=[x for x in L2 if x%5==0]
print(L3)
string="winter is coming".split()
print(string)
string_case=[[w.upper(),w.lower(),len(w) for w in string]]
for i in string_case:
    print(i)

list1=[1,'4' ,'g','a', 0 ,4]
square_int=[x**2 for x in list1 if type(x)==int]
print(square_int)
