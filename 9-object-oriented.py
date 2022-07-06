#  a class has many components. most important of which are attributes and functions.
# this clubbing together of functions and data forms the basis of OOP

#ATTRIBUTES AND FUCNTIONS
# one can percive a class as a prototpye and an object as an instance of a class
#for example 'movie' is a class
#and 'the iron-man' is an object
# a class has attributes and behaviours
# the attributes  generally store data and the behavoir is implemented using functions
# a class can be depicted using the class diagram having three parts,
#       1. the name
#       2. the attribute-depicts the characteristics of the entity that we are concerned with
#       3. the functions of a class- they implement the behavoir of a class

class movie:
    def getdata(self):
        self.name=input('enter name\t: ')
        self.year=int(input('enter the year\t: '))
        self.genre=input('enter genre\t: ')
        self.director=input('enter the director\'s name\t: ')
        self.producer=input('enter the producer\t: ')
        L=[]
        item=input('enter the name of the actor\t: ')
        L.append(item)
        choice=input('Press \'y\' for more \'n\' to quit')
        while(choice=="y"):
            item=input('enter the name of the actor\t: ')
            L.append(item)
            choice=input('enter \'y\' for more \'n\' to quit' )
        self.actor=L
        self.music_director=input('enter the name of the music director\t: ')


    def putdata(self):
        print('name\t: ',self.name)
        print('year\t: ',self.year)
        print('genre\t: ',self.genre)
        print('director\t: ',self.director)
        print('producer\t: ',self.producer)
        print('music_director\t: ',self.music_director)
        print('actors\t: ',self.actor)

m=movie()
m.getdata()
m.putdata()
# for object oriented programming a special function utilizes the value of the data members.
# this function generally has the same name as that of the class
# the function is called a constructor
# constructors can be of two types.
#       default constructor-doesnt take any parameters

#       parameterized constructor they take arguments and initialize the data members using those arguments
# when the lifetime of an object ends a destructor is called.
# a destructor being used in python i 'del'


# ELEMENTS OF OBJECT-ORIENTED PROGRAMMING

#CLASS- a real or virtual entity which has relevance to the problem at hand and has asharp physical boundaries
#OBJECT-consider a student management system that stores the data of each student of a school.
#       while entering data the operator would deal with an individual student, not the idea of a student.
#       the idea of the student is a class whereas the student is an instance of class or an object.
#       an object is an instance of a class. the objects interact with each other  and get the work done.
#       a class can have any number of objects
#ENCAPSULATION-the clubbing together of the data and the functions that operate on the data.
#       functions in a clas can be used in a variety of ways. their accessibilty of data members and member functions
#       can also be managed using access specifiers
#DATA HIDING-the accessibilty if data can be govered in a class. the data in the case  of procedural programming
#       is accessible throughout the program(global data).the data private to a class is one which can be accessed only by the members
#       of the class
#INHERITANCE-classes are made so thatv they can be subclassed. art of subdividing classes into subclasses is 
#           is called inheritance. each subclass can have functions and data that belongs to the sub class only.
#POLYMORPHISM-(manyforms) one  of the simplest examples is operator overloading
#               operator overloading means using the same operator in more than one way.
#               for example the '+' is used in summing integers and also in concatenating strings.
#REUSABILITY



