class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def printInorder(root):
        if root:
            #first recur on left child
            printInorder(root.left)
            #then print the data of node
            print(root.val,end=" "),
            #now recur on right child
            printInorder(root.right)
def printPostorder(root):
        if root:
            printPostorder(root.left)
            printPostorder(root.right)
            print(root.val,end=" "),
def printPreorder(root):
        if root:
            print(root.val,end=" "),
            printPreorder(root.left)
            printPreorder(root.right)
    
root = Node(100)
root.left=Node(400)
root.right=Node(500)
root.left.left=Node(700)
root.left.right=Node(600)
root.left.right.left=Node(900)
root.right.left=Node(800)
root.right.right=Node(200)
root.right.right.left=Node(300)
print("pre order")
printPreorder(root)
print()
print("in order")
printInorder(root)
print()
print("post order")
printPostorder(root)
print()