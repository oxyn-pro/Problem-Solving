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
node_4.next = node_2

# 1 -> 2 -> 3 -> 4 -> 2 ... cycle/infinite loop


# TC: O(n)
# SC: O(n)
def has_cycle_set(head):
    """This solution uses a hash set to store a node and
    check whetherthe next node's 'next' is contained in that set of hashes."""
    current_head = head
    nodes = set()

    while current_head:
        nodes.add(current_head)
        if current_head.next in nodes:
            return True
        current_head = current_head.next
    return False


has_cycle_set(head)


# TC: O(n)
# SC: O(1) - we just need to use slow and fast pointers
def has_cycle_floyd(head):
    """This solution uses a slow and fast pointer algorithm called 'Floyd's Tortoise and Hare'."""
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


has_cycle_floyd(head)
