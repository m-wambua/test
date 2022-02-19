# we will be iterating through a list and appending two other lists one for poitive integers and the other for negative integers

from asyncio import constants


L=[1,2,5,7,-1,3,-6,7]
p=[]
n=[]
for num in L:
    if (num>0):
        p.append(num)
    else :
        n.append(num)

print ('the list of positive numbers is \t :',p)
print('the list of negative numbers \t : ',n)

string=input('enter a string \t : ')
vowels=""
constant=""
for i in string:
    if ((i=='a') |(i=='e') |(i=='i')|(i=='o')|(i=='u')):
        vowels=vowels+str(i)

    else:
        constant=constant+str(i)

print('the vowels in your string is/are \t :',vowels)
print('the consonant(s) in your string is/are \t : ',constant)

# what about iteration in tuples

T=(1,2,3)
for i in T:
    print(i)
print (T)

##iteration through dictionaries
Dict={'Programming in C#':499,'Algorithm Analysis and Design':599}
print(Dict)
for i in Dict:
    print(i)
