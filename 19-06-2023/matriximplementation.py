n=int(input("Enter row of matrix"))
m=int(input("Enter column of matrix"))
l=[]
if(m==n):
    for i in range(n):
        l1=[]
        for j in range(m):
            x=int(input())
            l1.append(x)
        l.append(l1)
for i in range(len(l)):
    for j in range(len(l)):
        print(l[i][j],end="")
    print()
print("diagonal")
for i in range(len(l)):
    for j in range(len(l)):
        if(i==j):
            print(l[i][j],end=" ")
print("\nupper matrix")
for i in range(n):
    for j in range(m):
        if(i>j):
            print(l[i][j],end=" ")
print("\nlower matrix")
for i in range(n):
    for j in range(m):
        if(i<j):
            print(l[i][j],end=" ")
print("\nnon diagnal element")
for i in range(n):
    for j in range(m):
        if(i!=j):
            print(l[i][j],end=" ")