# using the get construct
# how this works is getting the values of the dictionary and then if one part of the dict is called and its comparred
# to what is on the right and the dont match up then it shows what it matches with
hbbooks={'programming in C#':2014,'algorithms':2015,'python':2016}
print(hbbooks.get('programming in C#','bad choice'))
print(hbbooks.get('algorithms','bad choice'))
print(hbbooks.get('python','bad choice'))
print(hbbooks.get('theory theory,all the way','bad choice'))




