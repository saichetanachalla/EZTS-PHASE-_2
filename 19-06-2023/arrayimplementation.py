l=[]
n=int(input("enter the size of array"))
for i in range(n):
    k=int(input())
    l.append(k)
print(l)
print("1.insert\n2.delete\n3.search\n4.sort\n5.display\n6.exit")
while(1):
    ch=int(input("enter choice\n"))
    if ch==1:
        m=int(input("enter the no.of elements"))
        for i in range(m):
              j=int(input())
              l.append(j)
        print("the updated array is",l)
    elif ch==2:
        j=int(input("enter the position of num to delete"))
        for i in range(len(l)):
            if i==j:
                del(l[i])
        print("the updated array is:",l)
    elif ch==3:
        p=int(input("enter the element to search"))
        c=0
        for i in range(len(l)):
            if i==p:
                c=+1
        if c>=1:
            print("the element is found")
        else:
            print("element not found")
    elif ch==4:
        print("the sorted array is",sorted(l))
    elif ch==5:
        print(l)
    elif ch==6:
        exit(0)
    else:
        print("invalid choice")