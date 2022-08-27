def give_space(n):
    for i in range(0,n):
        print(" ",end=" ")
nspace=0
nsteps = int(input("Enter number of steps"))
steps=[]
for i in range(0,nsteps):
    steps.append(int(input()))
print(steps)
for i1 in range(1,len(steps)+1):
    nspace=0
    for i2 in range(0,len(steps)-i1):
        nspace+=steps[i2]
    give_space(nspace)
    for i in range(0,steps[-i1]+1):
        print("*",end=" ")
    print()
    for i in range(0,steps[-i1]-1):
        give_space(nspace)
        print("*")
print("*")