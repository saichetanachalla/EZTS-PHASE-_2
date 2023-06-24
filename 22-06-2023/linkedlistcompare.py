class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert(head, data):
    if head is None:
        return Node(data)
    current = head
    while current.next:
        current = current.next
    current.next = Node(data)
    return head


def compare_lists(head1, head2):
    while head1 and head2:
        if head1.data != head2.data:
            return False
        head1 = head1.next
        head2 = head2.next
    # If one list is longer than the other
    if head1 or head2:
        return False
    return True


# Creating the first linked list: 1 -> 2 -> 3
head1 = None
head1 = insert(head1, 1)
head1 = insert(head1, 2)
head1 = insert(head1, 3)

# Creating the second linked list: 1 -> 2 -> 3
head2 = None
head2 = insert(head2, 1)
head2 = insert(head2, 2)
head2 = insert(head2, 3)

# Compare the two linked lists
if compare_lists(head1, head2):
    print("The linked lists are the same.")
else:
    print("The linked lists are not the same.")
