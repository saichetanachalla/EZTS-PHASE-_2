class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val==key:
            return root
        elif root.val<key:
            root.right = insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root
#inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)
def search(root,key):
    if root is None or root.val==key:#base cases:root is n ull or key is present at root
        return root
    if root.val<key:#key is greater than root's key
        return search(root.right,key)
    return search(root.left,key)#key is smaller than root's key

r=Node(100)
r=insert(r, 70)
r=insert(r, 50)
r=insert(r, 60)
r=insert(r, 9)
r=insert(r, -3)
inorder(r)
n=int(input())
if search(r, n) is None:
    print("not found")
else:
    print("found")
    
