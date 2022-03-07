
print('enter text, pass \'\\e\' to exit')
L=[]
i=1
in1=input('line number' +str(i)+'\t:')
while(in1 != '\e'):
    
    L.append(in1)
    i=i+1
    in1=input('line number'+str(i)+'\t:')
print(L)
f=open('line.txt' , 'w')
f.writelines(L)
f.close()
f=open('lines.txt','r')

for l in f.readlines():
    print(l , end=' ')

f.close()