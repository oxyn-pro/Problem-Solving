class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)

head.next = node_2
node_2.next = node_3
node_3.next = node_4


# TC: O(n)
# SC: O(1)
# 1 -> 2 -> 3 -> 4
# None <- 1 <- 2 <- 3 <- 4 -> None
def reverse_linked_list(head):
    current_node = head
    prev_node = None

    while current_node:
        nxt_node = current_node.next

        current_node.next = prev_node
        prev_node = current_node
        current_node = nxt_node

    return prev_node


reverse_linked_list(head)


# Recursive option:
# 1 -> 2 -> None
# 1 -> 2 -> 1
# <- 1 2 -> 1
# 2 -> 1 -> None


# TC: O(n)
# SC: O(n) - Because the call stack grows as the input grows.
# If there are 2 nodes, there will be 2 recursive calls, meaning the call stack size will be 2.
def rec_reverse_linked_lis(head):
    if not head:
        return None

    new_head = head
    if head.next:
        new_head = rec_reverse_linked_lis(head.next)
        head.next.next = head
    head.next = None

    return new_head


rec_reverse_linked_lis(head)
