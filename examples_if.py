# the following expression will be for a multi-valued function
fx='''
f(x)=x^2 +5x + 3, if x>2
    =x + 3 , if x<=2
'''
x = int(input('please enter the value of x \t: ' 'for the fucntion %s' %fx))# the change here was in order to display the fucntion
if x>2:
    f=((pow(x,2)) + (5*x) + 3)

else:
    f=x + 3

print('value of function f(x) = %d' %f)

