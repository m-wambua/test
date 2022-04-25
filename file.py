## file handling

f=open('test.txt','r')
print('name of the file\t:',f.name)
print('mode\t:',f.mode)
print('file closed?\t:',f.closed)
f.close()
print('mode\t:',f.mode)
print('file closed?\t:',f.closed)

import sys

from matplotlib.pyplot import flag
print('the number of arguments',len(sys.argv))
print('arguments\n')
for x in sys.argv:
    print('argument\t',x)

