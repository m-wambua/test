## say if we want to do patterns

# this will be used to undrstanc nested loops

q=int(input('enter the number of rows'))
    
for w in range (q):
    for e in range (1,w+2):
    
        print('*',end=" ")
    print()

r = int(input('enter the number of rows you want to display : '))
for y in range (r):
    for  u in range (1,y+2):
        print( y+1,end=" ")# dont know what this line does yet
    print()

a=int(input('enter the first element of your program : '))
for s in range(a):
    for d in range(1,s+2):
        print(d+1,end=" ")
    print()

f=int(input('enter the number of rows : '))
k=1
for g in range (f):
    for h in  range(1,g+2):
        print(k,end=" ")
        k=k+1
    print()

# what about a christmass tree
j = int(input('enter the nummber of rows you want your tree to be : '))
for k in range (j):
    for l in range(0,j-k-1):
        print(' ', end="")
    for z in range (0,2*k+1):
        print('*',end="")
    print()