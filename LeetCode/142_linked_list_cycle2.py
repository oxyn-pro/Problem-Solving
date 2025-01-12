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
# SC: O(1)
def detectCycle(head):
    """This solution uses a slow and fast pointer algorithm called 'Floyd's Tortoise and Hare'."""
    if not head or not head.next:
        return

    cycle_node = slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return

    while cycle_node != slow:
        slow = slow.next
        cycle_node = cycle_node.next

    return cycle_node


detectCycle(head)
