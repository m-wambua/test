### string operators

# the concantention operator(+)
# the cancentantion operator takes tow string and produces a concatenated string.
# the operator acts on value as well as variables

name=input('enter your name\t:')
result1='hi '+'there'
print(result1)
str1='hello'
str2=str1+' ' +name
print(str2)


# the replication operator
#replicates the strings as many times as the first operand
#the operator operates on two operands :the first being a number and the second being a  string

name= input('enter your name again\t:')
print('hi ', ' ', name)

str1=input('enter a string\t:')
num=int(input('enter a number \t :'))
result1=num*str1
print(result1)