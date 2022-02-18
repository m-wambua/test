authors=['michael','mutisya','wambua']
print(authors)
combined=[1,'two','many',3]
print(combined)
list=[]
print(list)

listoflist=[1,[2,3],4]
print(listoflist)
listoflist[-1]='is it imutable'# yes lists are very mutable
print(listoflist)


print(combined[2])
print(combined[-1])

#tupples

tup1=(2,3)
print(tup1)
(a,b)=tup1
print(tup1)
print('the first element is', a)
print('the second element is',b)
tup2=(101,'hari')
tup3=(102,'havi')
(code1,name1)= tup1
print(tup1)
(code2,name2)=tup2
print(tup2)
print('the code of',name1,'is',code1,'\nthe code of',name2,'is',code2)


print('enter the first number\t:')
num1= int(input())
print('enter the second number\t:')
num2=int(input())
print('\nthe number entered are',num1,'&',num2)
(num1,num2)=(num2,num1)# the swapping is done on the other side of the equal sign
print('\nthe numbers are now',num1,'&',num2)

tup4=(1,2)
tup5=(5,7)
tup6=tup4 +tup5# this concatinates
print(tup6)
tup7=tup4-tup5
print(tup7)