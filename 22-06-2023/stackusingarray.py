stack=[]#implementation of stacks using arrays
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
def peek():#or u can call it as pop
    if not stack:
        print("stack is empty")
    else:
        e=stack[-1]
        print("top element",e)
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