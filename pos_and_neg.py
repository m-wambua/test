# we will be iterating through a list and appending two other lists one for poitive integers and the other for negative integers

L=[1,2,5,7,-1,3,-6,7]
p=[]
n=[]
for num in L:
    if (num>0):
        p.append(num)
    elif (num<0):
        n.append(num)

print ('the list of positive numbers is \t :',p)
print('the list of negative numbers \t : ',n)