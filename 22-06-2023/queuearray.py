queue=[]#implementation of stacks using arrays
def enqueue():
    element=int(input("enter element"))
    queue.append(element)
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e=queue.pop(0)
        print("removed element",e)
def display():
    print(queue)

while(1):
    print("select option 1.enqueue 2.dequeue 3.display 4.quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("incorrect choice")
