# another way of doing the generator function is

L1=[x**3 for x in range (10)]
print(L1)
L2=[3**x for x in range (2,10,1)]#means move from 2 to 10 with increaments of 1
print(L2)
L3=[x for x in L2 if x%5==0]
print(L3)
string="winter is coming".split()
print(string)
string_case=[[w.upper(),w.lower(),len(w)] for w in string]
for i in string_case:
    print(i)

list1=[1,'4' ,'g','a', 0 ,4]
square_int=[x**2 for x in list1 if type(x)==int]
print(square_int)
# additional understanding of comprehensions is given by the following snippet code
L_cel=[21.2,56.6,89.2,90.1,78.1]
L_kelvin=[x +273.16 for x in L_cel]
print('The output list')
for i in L_kelvin:
    print (i)

## finding the cartssian product of two given sets

A=['a','b','c']
B=[1,2,3,4]
AXB=[(x,y)for x in A for y in B]
for i in AXB:
    print(i)