# implementing a search


def search(L, item):
    flag=0
    for i in L:
        if i==item:
            flag=1
            print('position ',i)
    if flag==0:
        print('not found')

L=[1,2,5,9,10]
search(L,5)
search(L,3)

## say we want to do a binary search
def binary_search(list,n):
    low=0
    high =len(list)-1

    mid = 0

    while low<=high:
        mid=(high+low)//2

        if list[mid]<n:
            low=mid+1

        elif list[mid]>n:
            high=mid-1

        else :
            return mid

    return -1


list=[12,24,32,39,45,50,54]

n= int(input('please enter the number you are looking for'))

result=binary_search(list,n)
if result!=-1:
    print('element is present at index'+str(result))

else:
    print('element is not part of the list')