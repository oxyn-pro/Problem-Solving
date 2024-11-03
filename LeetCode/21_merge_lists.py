class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


head = Node(1)
node_2 = Node(2)
node_3 = Node(4)

head.next = node_2
node_2.next = node_3

head2 = Node(1)
node2_2 = Node(3)
node2_3 = Node(4)

head2.next = node2_2
node2_2.next = node2_3


# TC: O(m+n) or simply O(n)
# SC: O(1)
# 1 -> 2 -> 4
# 1 -> 3 -> 4
# 0 -> 1 -> 1 -> 2 -> 3 -> 4 -> 4
def merge_lists(head1, head2):
    dummy_head = Node()
    tail = dummy_head

    while head1 and head2:
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    if head1:
        tail.next = head1
    else:
        tail.next = head2

    return dummy_head.next


merge_lists(head, head2)
