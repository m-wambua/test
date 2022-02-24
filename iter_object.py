# defining an iteratable object
# we can define a class in which __init__ , __iter__, and __next__ can be defined as per requirement
#__init__ function initializes the variable of the class
#__iter__ defines the mechanism of iterators
#__next__ implements the jump to the next item

class yrange:
    def _init_(self,n):
        self.a=int(input('enter the first term\t:'))
        self.d=int(input('enter the common difference \t:'))
        self.i=self.a
        self.n=n

    def _iter_(self):
        return self
    def _next_ (self):
        if self.i<self.n:
            i=self.i
            self.i=self.i + self.d
            return i
        else:
            raise StopIteration()

y=yrange
y._init_(y,8)
print(y)
print(y._next_(y))
print(y._next_(y))
print(y._next_(y))

        