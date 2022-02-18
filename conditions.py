## if ,if -else and if -elif-else

a= input('enter masks : ')

if int(a)> 40:
    print('pass')

else:
    print('fail')


num = int(input('Enter three digit number\t'))
if ((num<100) | (num>999)):
    print('you have not entered a number between 100 and 999')

else:
    flag=0
    o=num%10
    t=int(num/10)%10
    h=int(num/100)%10
    print('o\t:',str(o),'t\t:',str(t),'h\t:',str(h))
    rev=h+t*10+o*100
    print('number obtained by reversing the order of the digitd\t:',str(rev))

    sum1=num+rev
    print('sum of the number and that obtained by reversing the order of digits\t:',str(sum1))

    if sum1<1000:
        o1=sum1%10
        t1=int(sum1/10)%10
        h1=int(sum1/100)%10
        print('o1\t:',str(o1),'t1\t:',str(t1),'h1\t:',str(h1))

    if((o==o1) | (o==t1) | (o==h1) | (t==o1) | (t==t1) | (t==h1) | (h==o1)  | (h==t1) |(h==h1)):
        print('condition true')
        flag==1

    else:
        o1=sum1%10
        t1=int(sum1/10)%10
        h1=int(sum1/100)%10
        th1=int(sum1/1000)%10
        print('o1\t:',str(o1),'t1\t:',str(t1),'h1\t:',str(h1),'t1\t:',str(th1))

    if((o==o1) | (o==t1) | (o==h1) | (o==th1) | (t==o1) | (t==t1) | (t==h1) | (t==th1) | (h==o1) | (h==t1) | (h==h1) | (h==th1)):
        print('conditionn true')
        flag==1


    