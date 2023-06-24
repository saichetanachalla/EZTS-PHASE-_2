class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
        self.last_node=None
    def append(self,data):
        if self.last_node is None:
            self.head=Node(data)
            self.last_node=self.head
        else:
            self.last_node.next=Node(data)
            self.last_node=self.last_node.next
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end=" ")
            current=current.next
a_llist=Linkedlist()
n=int(input("how many elements do you want to enter"))
for i in range(n):
    data=int(input("enter data item"))
    a_llist.append(data)
print("the linked list:",end=" ")
a_llist.display()