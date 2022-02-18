# handling lists using loops
hb=["Programming in C#",["Oxford University Press",2015]]
rm=["SE is everything",["obscure publishers", 2015]]
authors=[hb, rm]

print(authors)
for i in range (len(authors)):
    for j in range(len(authors[i])):
        for k  in range(len(authors[i][j])):
            print (str(i)+" "+str(j)+" "+str(k)+ " "+str(authors[i][j][k])+ "\n")
            
print()
