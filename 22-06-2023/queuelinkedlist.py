class Node: 
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
        self.last=None
    def enqueue(self,data):
        if self.last is None:
            self.head=Node(data)
            self.last=self.head
        else:
            self.last.next=Node(data)
            self.last=self.last.next
    def dequeue(self):
        if self.head is None:
            return None
        else:
            toreturn=self.head.data
            self.head=self.head.next
            return toreturn
obj=Queue()
while(1):
    print("enqueue<value>")
    print("dequeue")
    print("quit")
    do=input("what would you like to enter").split()
    print("do",do)
    print("do[0]",do[0])
    operation=do[0].strip().lower()
    if operation == "enqueue":
        obj.enqueue(int(do[1]))
    elif operation == "dequeue":
        toreturn=obj.dequeue()
        if toreturn is None:
            print("stack is empty")
        else:
            print("popped value: ", int(toreturn))
    elif operation=="quit":
        break
    else:
        print("incorrect input")
    
        
            
