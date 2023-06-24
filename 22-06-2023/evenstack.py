stack=[]#implementation of stacks using arrays
odd=[]
even=[]
def push():
    element=int(input("enter element"))
    stack.append(element)
def popelement():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("removed element",e)
def display():
    print(stack)
    print("1 or 2")
    n=int(input())
    if n==1:
        for i in stack:
            if i%2==0:
                even.append(i)
    if n==2:
        for j in stack:
            if j%2!=0:
                odd.append(j)
    print(even)
    print(odd)
while(1):
    print("select option 1.push 2.pop 3.display 4.peek 5.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        popelement()
    elif choice==3:
        display()
    elif choice==4:
        peek()
    elif choice==5:
        break
    else:
        print("incorrect choice")