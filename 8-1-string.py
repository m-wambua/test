# a program to transverse through strings
# writing for i <string> helps us to access one character at a time from a given string.
# the variable 'str1' stores the string enterd by the user and it is iterated  using the for loop

str1=input('enter a string\t:')
for i in str1:
    print('character \t:',i)

# the above methodology can be used ti find the length of string although there is a built in function for such
name= input('enter  your name\t:')
length=0
for i in name:
    length=length+1
print('the length of your\t',name,'is\t:',length)## puttting this in the indentation of the for loop repeats the name i times

## what about displacement

str1=input('enter another string\t:')
k=int(input('enter a value of k\t:'))
i=0
str2=""
while i<len(str1):
    str2+=str1[(i+k)%len(str1)]
    print(str2)
    i+=1
    
print(str2)
