# asking a user to enter a string and replacing  each character by that obtained by adding tow to the ASCII
# value of that character
str3=input('enter the string\t: ')
k= ascii(input('enter the value of k\t:'))
y=0
str4=""
while y<len(str3):
    str4+=str((ascii(str3[y])+k))
    print(str4)
    y+=1
print(str4)