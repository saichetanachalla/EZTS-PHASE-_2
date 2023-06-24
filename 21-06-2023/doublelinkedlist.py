class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class doublell:
    def __init__(self):
        self.head=None
    
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                if temp.next!=None:
                    print("<->",end=" ")
                temp=temp.next
    def insertatbegin(self):
        n=node(300)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
    def insertatend(self):
        n=node(30)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp
    def insertatpos(self,pos):
        n=node(44)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.prev=temp#44's prev=10
        n.next=temp.next#44's next=20
        temp.next.prev=n#20's prev=44
        temp.next=n#10's next 44
    def deleteatbegin(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def deleteatend(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
        temp.prev=None
    def deleteatpos(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=prev.next
    def reverse(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            while temp:
                     print(temp.data,end=" ")
                     if temp.prev!=None:
                      print("<-->",end=" ")
                     temp=temp.prev

obj=doublell()
n=node(10)
obj.head=n
n1=node(20)
n.next=n1
n1.prev=n
n2=node(30)
n1.next=n2
n2.prev=n1
n3=node(40)
n2.next=n3
n3.prev=n2
n4=node(50)
n3.next=n4
n4.prev=n3
n5=node(60)
n4.next=n5
n5.prev=n4
obj.display()
obj.insertatbegin()
print("\nafter inserting at begining\n")
obj.display()
obj.insertatend()
print("\nafter inserting at end\n")
obj.display()
obj.insertatpos(3)
print("\nafter inserting at pos\n")
obj.display()
obj.deleteatbegin()
print("\nafter deleting at begin\n")
obj.display()
obj.deleteatend()
print("\nafter deleting at end\n")
obj.display()
obj.deleteatpos(2)
print("\nafter deleting at pos\n")
obj.display()
print("\nprinting reverse\n")
obj.reverse()