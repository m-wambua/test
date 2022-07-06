#INTRODUCTION TO CLASSES
#classes are real or virtual entitites which have an importance to the problem at hand and a sharp physical boundary.
# a class in python can hold any kind and any amount of data
# a class in python can be subclassed. all type of inheritance, including multiple inheritance are supported in python.
# method overriding is also allowed in python
# in a class all data members are public in nature
# member fucntions in a class are all virtual
#in a class all member functions must have the first argument as the object representing that class from now on referred to as 'self'


# DEFINING A CLASS
#SYNTAX IS AS FOLLOWS
# class <name of the class>:
#       def <function name>(<arguments>):
#           <block of code>
#       <members>

# Every function in the class must have at least one argument,self.
# A class definition has functions but ca also have other members
#The  Attribute of an object is data attribute, and the function that belongs to an object is method

## Creating an object
### An object is created by associating a name with an instance of the class, initialized uing the default constructor.
# for example
# e1=employee()
# e1 is the name of the pbject and employee() is the constructor of the class
# the creation of a class is called instantiation.
# the function of a class can be called using the dot operator with a given class.
# as an example , to call the getdata() function of the employee class the following statement are used.
# e1.getdata()
# other methods of the class can be called using the dot operator

class employee:
    def getdata(self):
        self.name=input('enter name\t: ')
        self.age=input('enter age\t:')
    def putdata(self):
        print('name\t:',self.name)
        print('Age\t:',self.age)
e1=employee()
e1.getdata()
e1.putdata()

#scope of data members
# The scope of a namespace is the region where it is directly accessible.
# In determining the scope of a namespace, the following rules are followed:
#       1. the innermost scope is searched
#       2.scope of enclosing fucntions are searched
#       3.the global namespaces are searched
#       4.the built-in names are seen
# the non-local statements rebind the variables in the global scope.

class demo_class:
    a=5
    def getdata(self,b):
        a=7
        self.b=b
    def putdata(self):
        print('the value of \'a\' is    ' 'a' 'and that of \'b\' is', self.b)
d=demo_class()
d.getdata(9)
d.putdata()

## from the above code it can be stated that:
## the value of a for all instances of the class is 5, until a function changes the value of a is called
## in putdata() a does not exist , a is local to getdata()
## b can be accessed in both the functions as b is a data member of the class(note that every time b is called, 'self.b' is used)
## so for the above code to work the indentation of lines 60-62 should be shifted to the left

## such that in the following code, 'a' is common for all the classes.
#'b' is a member of the class
#Here,'self.b=b' means the data member 'b' of the class(self.b) is assigned the value 'b' , 
#which is the second argument of the function getdata()
#'c' is local to getdata(), so 'c' of getdata() is not same as that of putdata()

#DEFENITION: INTANCE VARIBALE AND CLASS VARIABLE
# An instance variable is one which is unique to each instance and a class variable is one which is shared  by all instances.

class demo_class_2:
    a=5
    def getdata_1(self,b):
        c=7
        self.b=b
        print('\'c\' is ',c,' and \'b\' is ',self.b)
    def other_function(self):
        c=3
        print('value',c)
    def putdata_1(self):
        print('\'b\' ''is',self.b)
d=demo_class_2()
d.getdata_1(9)
print(d.a)
d.other_function()
d.putdata_1()
e=demo_class_2()
print(e.a)



# A global data member can be made outside the class which is accessible to all the 
# methods(untils the scope of the data member is changed)
# In the code above 'a' is common for all instances of the class,
#'b' is the data member of the class and 'c' is a local variable.

#NESTING
# The design of a class requires conceptualization of an entity, which has attribute and behavior.
# The object of a class can be made in another class also.
#A class can also have the objects of another class as its members. This is called nesting.
# The attributes of a class can themsleves be entities.
class date:
    def getdata_2(self):
        self.dd=input('enter date (dd)\t: ')
        self.mm=input('enter month (mm)\t: ')
        self.yy=input('enter year (yy)\t: ')
    def display(self):
        print(self.dd,':',self.mm,':',self.yy)
class student:
    def getdata_2(self):
        self.name=input('enter name\t: ')
        self.dob=date()
        self.dob.getdata_2()
    def putdata_2(self):
        print('name \t:',self.name)
        self.dob.display()

s=student()
s.getdata_2()
s.putdata_2()
# never forget to put the brackets!!!

#CONSTRUCTOR
# Note that each time a class is instantiated a constructor is used. 
#There are two types of constructors:
#       Default- does not take any argument. in python the constructors are called using the functions having the same name
#               as that of the class.However they are implemented by making the __init__() function inside the class.
class employee_1:
    def getdata_3(self):
        self.name=input('enter name\t: ')
        self.age=input('enter age\t: ')
    def putdata_3(self):
        print('name\t:',self.name)
        print('age\t:',self.age)
    def __init__(self):
        self.name='ABC'
        self.age=20
e1=employee_1()
e1.getdata_3()
e1.putdata_3()
e2=employee_1()
e2.putdata_3()

# In the code above the object e1 behaves as expected.the values entered by the user in the getdata() 
#fucntion are displayed when putdata() is called.
# In the case of e2 the function getdata() is not called, therefore the value assigned in __init__ are displayed.

#

#       parameterized- is one which takes arguments, for example in the code above takes two parameters,
#                       name and age. in order to  assign the values to the object, the instantiation must be of the form:
#                       e2=employee_1('victoria', 22)
# Note that while defining the parameterized __init__, the first parameter is always 'self' and the rest of the parameters are 
#the values to be assigned to different data members of the class .
# In the case of employee class, three parameters 'self' , 'name' and 'age' are given.

class employee_3:
    def getdata_4(self):
        self.name=input('enter name\t: ')
        self.age=input('enter age\t: ')
    def putdata_4(self):
        print('name\t: ',self.name)
        print('age\t: ',self.age)
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def _del__():
        print('done')

e2=employee_3('Victoria',22)
e2.putdata_4()

# CONSTRUCTOR OVERLOADING
# Having the same name function in a class with a different number of parameters, or different types of parameters, is called fucntion overloading.
# In python, however, we cannot have more than one __init__ in a class

# Having studies the importance and implentation of constructors, let us now implement a constructor and let's consider
#the 'movie' class.
class movie:
    def getdata_5(self):
        self.name=input('enter name\t: ')
        self.year=input('enter year\t: ')
        self.genre=input('enter genre\t: ')
        self.director=input('enter the name of the director\t: ')
        self.producer=input('enter the producer\t: ')
        L=[]
        item=input('enter the name of the actor\t: ')
        L.append(item)
        choice=input('Press \'y\' for more \'n\' to quit')
        while(choice=='y'):
            item=input('enter the name of the actor\t: ')
            L.append(item)
            choice=input('enter \'y\' for more \'n\' to quit')
        self.actors=L
        self.music_director=input('enter the name of the music director\t: ')

    def putdata_5(self):
        print('name\t: ', self.name)
        print('year\t: ',self.year)
        print('genre\t: ',self.genre)
        print('director\t: ',self.director)
        print('producer\t: ',self.producer)
        print('actors\t: ',self.actors)

    def __init__(self):
        self.name='Fault'
        self.year=2015
        self.genre='Drama'
        self.director='XYZ'
        self.producer='ABC'
        self.music_director='LMN'
        self.actors=['A1','A2','A3','A4']
m=movie()
m.putdata_5()



