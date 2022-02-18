# so we will start working in fucntions




def product (num1,num2):#
    prod=num1*num2
    print ('The product of the numbers is \t: '+str(prod))

num1=int(input('enter the first number\t :'))
num2=int(input('enter the second number \t:  '))
print('calling the function....')
product(num1,num2)

print('back to the calling function')
## a function that does nothing but just print itself


def Ecclesiastes_3():#type(1 function)
    print("""
    To everything there is a season \n
    A time for every purpose under Heaven \n
    A time to be born\n
    and a time to die \n
    A time to plan \n
    and a time to reap \n
    A time to kill\n
    and a time to heal \n
    a time to breakdown \n
    and a time to build up \n
    a time to cast  away stones \n
    and a time to gather stones \n
    a time to embrace  \n
    and a time to refrain \n
    a time to gain \n
    and a time to lose \n
    a time to keep \n 
    and a time to cast away \n
    a time of love \n
    and a time  of hate \n
    a time of war \n
    and a time of peace \n


    """)

print('calling function \n')
Ecclesiastes_3()
print('calling function again \n')
Ecclesiastes_3()



def sum1():
    num1=int(input('enter the  first number : \t'))
    num2=int(input('enter the second number  : \t'))
    sum=num1+num2
    print('the sum of the number is \t :'+str(sum))

def sum2(num1,num2):
    sum=num2+num1
    print('the sum of the numbers is \t :'+str(sum))

def sum3(num1,num2):
    sum=num1+num2
    return(sum)

print('calling the first function ')
sum1()# because part of the function has the user input in it  one will jus be prompted to key in the two number you wantb to get the sum
num1=int(input('enter the first element \t :'))
num2=int(input('enter the second element \t :'))
print('calling the second function...')
sum2(num1,num2)#one will need to declare the inputs outside the function and then use those parameters inside the fucntion itself
print('calling the third function...')
results=sum3(num1,num2)# since this function returns the sum it has to be reassigned a new name before actually calling it

print(results)
def sum4(num_1,num_2):
    return(num_1+num_2)

print('using interger arguments \t : result :'+str(sum4(2,3)))
print('calling the function with string arguments \t: Result :  '+str(sum4('this','world')))


# implementing search