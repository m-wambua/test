
import sys

def sort(L):# sorting numbers using bubble sort
    i=0
    while(i<(len(L)-1)):
        print('\n iteration\t:',i,'\n');
        j=0
        flag=0
        while(j<(len(L)-i-1)):
            if (L[j]<L[j+1]):
                flag=1
                temp=L[j]
                L[j]=L[j+1]
                L[j+1]=temp
            print(L[j],end=' ')
            i=j+1
            print(L)
            if (flag==0):break
            i=i+1
        return (L)

    L=[1,5,23,45,12,34,78,35,9,64,40]
    for y in sys.argv:
        L.append(y)
        
    print('before sorting\t:',L)
    print(sort(L))
