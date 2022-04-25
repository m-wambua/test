# is done iter
L=[1,2,3,-4,-5,-6]
p=[]
n=[]
t=iter(L)
l1=[3,6,1,8,5]
l2=[7,4,6,2,9]
i1=iter(l1)
i2=iter(l2)
l3=sorted(list(i1)+list(i2))
print('list1 -',l1,'\nlist2-',l2,'\nsortedcombn -',l3)
try:# so what does the try do what it does is Hadling Exception (possibility for  a program handle selected exceptions
    #)
    while True:
        x=t.__next__()
        if x >=0:
                p.append(x)
        else:
            n.append(x)

except StopIteration:
    print('original List-',L,'\nList containing the positive numbers-',p,'\nLiat containing the negative numbers-',n)
    raise StopIteration

# the above was on numbers what about strings
#for some reason if i do strings below here it doesnt work

# say we want to concanate 2 lists into one by iterationg over individual elements of the lists using the list function and then
#then sortsthe concanates


