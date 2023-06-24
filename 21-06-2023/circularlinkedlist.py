class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlell:
    def __init__(self):
        self.head=None
    def insertatbegin(self,data):
        nb=node(data)
        nb.next=self.head
        self.head=nb
    def insertatend(self,data):
        nb=node(data)
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=nb
        nb.next=None  
    def insertatpos(self,data,pos):
        nb=node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        nb.next=temp.next
        temp.next=nb
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                if temp.next!=None:
                    print("->",end=" ")
                temp=temp.next
                
                
obj=singlell()
n=node(10)
obj.head=n
n1=node(20)
n.next=n1
n2=node(30)
n1.next=n2
n3=node(40)
n2.next=n3
n4=node(50)
n3.next=n4
n5=node(60)
n4.next=n5
n5.next=n
obj.display()
print("after inserting at beginning\n")
obj.insertatbegin(100)
obj.display()
print("after inserting at end")
obj.insertatend(50)
obj.display()
print("\ninsertion at given postion ")
obj.insertatpos(1000,4)
obj.display()
