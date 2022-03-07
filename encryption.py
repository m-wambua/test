f=open('textFile.txt','w')
f.write('hi there how are you')
f.close()
k=int(input('enter a number \t :'))
f=open('textFile.txt','r')
f1=open('textFile.txt','w')
for s in f.read():
    for c in s:
        print('character',c,'Ascii value\t:',ord(c))
        f1.write(str(chr(ord(c)+k)))

f1.close()
print((open('textFile.txt').read()))
f1=open('textFile1.txt','r')
f2=open('textFile2.txt','w')
for s in f1.read():
    for c in s:
        print('character ',c,'Ascii value\t:',ord(c))
        f2.write(str(chr(ord(c)-k)))

f2.close()
print((open('textFile2.txt').read()))