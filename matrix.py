# so lets say we want to use nested loops in matrces
n=int(input('enter the number of rows : '))
m=int(input('enter the number of columns : '))
a=1
for i in range(n):
    for j in range(m):
        
        for k in range (m):
            element=int(input('you may start keying in the values : '))
            a=a+1
            print(element,sep=' ',end=' ')

    for l in range (n):
        element=int(input())
        a=a+1
        print(element,sep=' ',end=' ')
    print()