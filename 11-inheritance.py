#INTRODUCTION TO INHERITANCE AND COMPOSITION
# The class from which class(es) are derived from is called a base class and those that inherit features 
# from the base class are derived classes.
#The derived class can use the modules of the base class in a variety of ways as will be discussed:


# INHERITANCE AND METHODS
# As far as modules are cobcerned, inheritance can help the programmer ti derive the features by one of the 
# following ways.
#       The method is not present in the child class, but only in the parent class: in such cases
#       if an instance of the child class calss the said method, the parent class's method is called.

class ABC:
    def show(self):
        print("Show ABC")
class XYZ(ABC):
    def show1(self):
        print("Show XYZ")

A=ABC()
A.show()
B=XYZ() 
B.show()
B.show1()

# In the above code snippet the derived class does not have a  method called show() so calling show using an instance
# of the derived class(consider, in this case) calls the method of the parent class.

# A second way this can be done is  when:
#       The method is present in both the parent class and in the derived class:in such cases, if this mehtod
#       is invoked using  an instance of the derived class then the method of the derived class is called.
#       If the method is called using an instance of the base class, the method of the base class is called.
#       Note that in such cases, the derived class redifines the method.This ovveriding ensures that the search
#       of the method in the inheritance tree ends up invoking this method only


class ABCD:
    def show(self):
        print("show of ABCD")
class WXYZ(ABCD):
    def show(self):
        print("show of WXYZ")

A=ABCD()
A.show()
B=WXYZ()
B.show()

#    In the above snippet x.show()calls the show() method of the derived class,whereas y.show() calls the method of the vase class.

#       The inherited class modifies the method of the base class and in the process invokes the method of the base
#       class inside the method of the derived class also.

class ABCDE:
    def show(self):
        print("show off ABCDE")
class VWXYZ(ABCDE):
    def show(self):
        print("something before calling the base class function")

#ABC.show(self) when uncommented this line gives an error.
print("something after calling the base function")
A=ABCDE()
A.show()
B=VWXYZ()
B.show() 

# The first type of inheritance will henceforth be referred to as implicit inheritance.
#In this type , the method of the base class can be called using an instance of the derived class.

# The second type of inheritance will henceforth be referref to as explicit overriding.
# And as stated earlier, the derived class will redefine the method of the base class and calling this method
# using an instance of the derived class will invoke the method of the derived class.

# The third type of inheritance is the most important and practical form of overriding methods.
#This type of inheritance leaves the room of not making an instance of the base class, if not required, still
#using the function

# The following code combines the three types of inheritance.

class Student:
    def __init__(self,name):

        self.name=name
    def show(self):
        print("name\t: "+self.name)
    def random(self):
        print("A random method in the base class")

class RegularStudent(Student):
    def __init__(self, name):## override the base class method and cass the base class method
        self.age=22

        Student.__init__(self,name)

    def show(self):## redifines the base class method
        print("name (derived class)\t: "+self.name+"Age\t: "+str(self.age))

    def random(self):## nothing to do with the base class method
        print("Random method in the derived class")

naks=Student("Victoria")
hari=RegularStudent("Vickie")
naks.show()
hari.show()
## The variable can be seen outside the clas also
print(naks.name)
print(hari.name)

# Here we created a class called Student having __init__ and show methods.The Student class should have a 
# a data member callled name. The __init__ should assign value to name and show should display the value. Create
# another class called RegularStudent, which will be the derived class of the Student class.
#The class should have two methods __init__ and show. The __init__ should assign values to age and should call
# the __init__ of the base class and pass the value of the name to the base class.The show method must display
#  the data of the RegularStudent. In additoion to the above both classes should have methods called random,
#both of which should be independent of each other.


#COMPOSITION.

#Making an instance of another class inside a class makes things easy and helps the programmer 
#to accomplish many tasks.
#Consider that a Student and his PhDguide are subclasses of the person class. Also, the data
# of the PhDguide includes the list of students guided by him/her.This is where composition comes into play.
# The instansiation of the students in the PhDguide class can be done as will be explained below.
# 
# 
class Student: 
    def __init__(self,name,email):
        self.name=name
        self.email=email
        
    def putdata(self):
        #self.name=input("please enter your name\t: ")
        #self.email=input("please enter your email address\t: ")
        print("the students name is\t: ",self.name,"and their email adress is\t:",self.email)

class PhDguide:
    def __init__(self,name,email,students):
        self.name=name
        self.email=email
        self.students=students

    def putdata(self):
        print("\nGuide Data\nName\t:",self.name,"\nE-mail\t:",self.email)
        print("\nList of student\n")
        for s in self.students:
            print("\t",s.name,"\t",s.email)


    def add(self,students):
        s=Student(students.name,students.email)
        if s not in self.students:
            self.students.append(s)


    def remove(self,students):
        s=Student(students.name,students.email)
        flag=0
        for s1 in self.students:
            if(s1.email==s.email):
                print(s,"removed")
                self.students.remove(s1)
                flag=1

        if flag==0:
            print("not found")

Harsh=Student("Harsh","harsh@yahoo.com")
Nav=Student("Nav","nav@yahoo.com")
Naks=Student("Nakui","nakui@yahoo.com")
print("\nDetails of students\n")
Harsh.putdata()
Naks.putdata()
Nav.putdata()
KKA=PhDguide("KKA","KKA@yahoo.com",[])
MU=PhDguide("Moin Uddin","profmoin@yahoo.com",[])
print("details of guides")
KKA.putdata()
MU.putdata()
MU.add(Harsh)
MU.add(Nav)
KKA.add(Naks)
print("Details of Guides (after the addition)")
KKA.putdata()
MU.putdata()
MU.remove(Harsh)
KKA.add(Harsh)
print("Details of Guides")
KKA.putdata()
MU.putdata()        

##INHERITANCE : IMPORTANCE AND TYPES
# A class has attributes (data members) and behavoir(class methods). However, at times these classes must be 
# extended to be able  to solve some specific problem without having to meddle with the original class.
# To be able to do so the language should be able to support inheritance.

# Using inheritance one can create new classes(derivedd classes) from an existing class(base class)
# Note that a derived class can have even more thnna one base class, referred to as a multiple inheritance
# ,which is one of the most undesirabled forms of inheritance. Also a base class cna itself be a derived class of some other class.
# The derived class will have all the allowed features of the base class plus some features of its own.
# A class generally has three sections, the first has the name of the class, the second section has attributes 
# and the third has the class methods#

# THE NEED FOR INHERITANCE
# In  really large programs , its difficult to code and debug a class.Once the programmer has crafted a class, there
# is little need to meddle with it. If one needs to craft a class having the same features as the class
# that has been developed(and add some more features to it), then it makes sense to derive classes from existing
# class.Inhertiance helps to reuse a code.One can also develop his class by extending classes developed by others.
#Thas is inheritance helps in distributing libraries.Ihenritance can also help to impelemnt a design that is more intuitive, better
# and more practical.

#TYPES OF INHERITANCE
# 1. simple inheritnace-has a singlr base class and a single derived class#

class book:
    def getdata(self):
        self.name=input("\nEnter the name of the book\t:")
        self.n=int(input("\nEnter the number of authors\t:"))
        self.authors=[]
        i=0
        while i<self.n:
            author=input(str("\nEnter the name of the "+str(i)+"th author\t:"))
            self.authors.append(author)
            i+=1
        self.publisher=input("\nEnter the name of the publisher\t:")
        self.ISBN=input("\nEnter the ISBN\t:")
        self.year=input("\nEnter year of publication\t:")

    def putdata(self):
        print("\nName\t:" ,self.name,"\nAuthor(s)\t:",self.authors,"\nPublisher\t:",self.publisher,"\nYear\t:",self.year,"\nISBN\t:",self.ISBN)

class Text_Book(book):
    def getdata(self):
        self.course=input("\nEnter the course\t:")
        book.getdata(self)
    def putdata(self):
        book.putdata(self)
        print("\nCourse\t:",self.course)

Book1=book()
Book1.getdata()
Book1.putdata()
Textbook1=Text_Book()
Textbook1.getdata()
Textbook1.putdata()

#The above illustration has two classes: book and Text_Book.The book class has two methods:getdata and putdata
# The getdata method asks the user to enter the name of the book ,number of authors,the list of authors,publishers,
#ISBN and year. The derived  class Text_Book has another attribute called course.The  getdata and the putdata methods extend the base class
# methods extend the base class methods(refer to the previous section)


#2.Hierarchical inheritance
#Here, a single base class has at least two derived classes. The following illustration has three classes:
#staff,teaching and non-teaching.Both teaching and non-teaching class are derived classes of the staff class.
#The staff class has two methods: getdata and putdata.The getdata metods asks the user to enter the name and 
# the salary of the member of the staff.The derived class teaching has another class called subbject.The getdata
# and the putdata methods extend the base class methods.Similarly,the derived class non-teaching has an attribute called department.
#The getdata and tge putdata methods extend the base class mehtods.

class staff:
    def getdata(self):
        self.name=input("\nEnter the name\t:")
        self.salary=float(input("\nEnter salary\t:"))

    def putdata(self):
        print("\nName\t:",self.name,"\nSalary\t:",self.salary)

    
class Teaching(staff):
    def getdata(self):
        self.subject=input("\nEnter subject\t:")
        staff.getdata(self)
    def putdata(self):
        staff.putdata(self)
        print("\nSubject\t:",self.subject)

class NonTeaching(staff):
    def getdata(self):
        self.department=input("\nEnter department\t:")
        staff.getdata(self)
    def putdata(self):
        staff.putdata(self)
        print("\nDepartment\t:",self.department)

X=staff()
X.getdata()
X.putdata()
##Teacher
Y=Teaching()
Y.getdata()
Y.putdata()
##Non Teaching staff
Z=NonTeaching()
Z.getdata()
Z.putdata()


#3.Multilevel inheritance-here a base class has a derived class which themselves becomes a base class 
# for some other class.The following illudtration hasd three classes:Person,emlpoyee and programmer.
# The person class is the base class.The employee class has been dreived fom the person class.
# The programmer class has been derived  from the employee class.
# The person class has two attributes-name and age and tow methods getdata and putdata.
# The getdtata method asks the user  to enter the name and the age of the member of the staff.The derived
# class emlpoyee has another attribute called emp_code.The getdata and the putdata methods extend the bae class
# methods.Similarly, the class programmer has another attribute called language.The getdata and the putdata
# methods extend its base class methods(Employee class)#

class person:
    def getdata(self):
        self.name=input("\nEnter the name\t:")
        self.age=int(input("\nEnter age\t:"))
    def putdata(self):
        print("\nName\t:",self.name,"\nage\t:",str(self.age))

class employee(person):
    def getdata(self):
        person.getdata(self)
        self.emp_code=input("\nEnter employee code\t:")

    def putdata(self):
        person.putdata(self)
        print("\nEmployee code\t:",self.emp_code)

class programmer(employee):
    def getdata(self):
        employee.getdata(self)
        self.language=input("\nEnter language\t:")
        
    def putdata(self):
        employee.putdata(self)
        print("znLanguage\t:",self.language)

A=person()
print("\nA is a person\nEnter data\n")
A.getdata()
A.putdata()
B=employee()
print("\nB is an emlpoyee and hence a person\nEnter data\n")
B.getdata()
B.putdata()
C=programmer()
print("\nC is a programmer hebce an emlpoyee and employee is a person\nEnter data\n")
C.getdata()
C.putdata()

#4.Multiple inheritance and Hybrid inheritance
# In multiple inheritance a class can be dreived form more than one base class.This type of inherutance can 
# be problematic as it can lead to ambiguity.It is therefore adviced to avoid this kind of inheritance as far
# as possible.In the following two classes B and C have been derived from class A.However, for the class D, the
#classes B and C are the base classes.This is an example of combining hierachal and multiple inheritance.



#METHODS
#Methods are just but functions with a special positional parameter within a class.Methods in fact, help
# the programmer to accomplish many tasks.Methods can be bound or unbound.The unboud methods do not have 
# 'self' as a parameter.While calling such methods the first argument must be the instance of the  class itself.
# The bound methods have 'self' as their first positional parameter when a method is accessed through 
# qualifing an instance of a class.Here, the instance of the class needs not be passed.Inspite the above 
# differences the following similarities between the two may not be missed:
# a. A method in python is also an object.Both bound and unbound methods are objects 
# b. The same methods can be invoked as a bound method and an unbound method.The discussion and illustration
# that follow will clarify the second point#
# 

#1.Bound Methods-if the first positional parameter of the methods is 'self'  its a bound method.
# In such cases , the instance of the class can call the method by passing the requisite parameters
# A variable which holds <object name>.<method name> can aslo be used to invoke the method.A method can also
# be invoked by creating an unmanned instance of the class.the third call of the display method depicts this 
# way of calling method
# This can be seen in the illustration below where a class called student has a display method,which takes
# two arguments-the first  being the positional parameter and the second being a string that is printed
# Note that the display methodis a bound method and hence is called through an instance of the class.#

class Student:
    def display(self,something):
        print("\n"+something)

## Invoking a bound method
Hari=Student()
Hari.display("Hi i am Hari")
## display() can also be invoked through an instance of the method
X=Hari.display
X("Hi i am through X")
##display called again
Student().display("calling display again")

#2.Unbound Method
#An unbound method does not have self.Thereforr the positional parameter needs not to be passed in method.
# In such methods, the variables should not be qualified by 'self'. Calling such methods in the same way as 
# before will result in errors.Such methods must be called  by the name of the class and not the object.
# Also note that that normal functions can be called using the class of which they are members. In the
# following illustration an unbound we shall use an unbound method getdata.#

class Student:
    def display(self,something):
        print("\n"+something)

    def getdata(name,age):
        print("\nName\t:",name,"\nAge\t:",str(age))

##Creating a new student
Naved=Student()
name=input("\nEnter the name of the student\t:")
age=int(input("\nEnter the age of the student\t:"))
Student.getdata(name,age)


#Methods are callable objects.
#Mthods ,like any other object in python can be stored in a list and called as per the requirement.
# In the illustration that follows the class operations has a constructor __init__(self,number),
# which assigns the value  of the second parameter to the data member called number.The class has
# two methods square and cube.The first method calculates(and returns) the square of the number and the second
# calculates(and returns) the cube of the number.Two instances of the class operations have been created :
# X and Y.X is intialized  to 5 and Y to 4.The elements of the list are then called one by one and invoked
# #

class operations:
    def __init__(self,number):
        self.number=number

    def square(self):
        return(self.number*self.number)
    def cube(self):
        return(self.number*self.number*self.number)

num1=operations(5)
num2=operations(4)
List=[num1.square,num1.cube,num2.square,num2.cube]
for callable_object in List:
    print(callable_object)








