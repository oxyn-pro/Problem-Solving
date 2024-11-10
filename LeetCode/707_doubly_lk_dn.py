class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:
    """Doubly Linked list WITH Dummy Heads"""

    def __init__(self):
        """It creates 2 dummy nodes and points them to each other:
        0 -> <- 0"""
        self.left = ListNode()  # Dummy head
        self.right = ListNode()  # Dummy head
        self.left.next = self.right
        self.right.prev = self.left

    # TC: O(n)
    # SC: O(1)
    def get(self, index: int) -> int:
        current_node = self.left.next

        while current_node and index > 0:
            current_node = current_node.next
            index -= 1

        while current_node and current_node != self.right and index == 0:
            return current_node.val

        return -1

    # TC: O(1)
    # SC: O(1)
    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)

        next_node = self.left.next

        self.left.next = new_node
        new_node.prev = self.left

        next_node.prev = new_node
        new_node.next = next_node

    # TC: O(1)
    # SC: O(1)
    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)

        prev_node = self.right.prev

        prev_node.next = new_node
        new_node.prev = prev_node

        self.right.prev = new_node
        new_node.next = self.right

    # TC: O(n)
    # SC: O(1)
    def addAtIndex(self, index: int, val: int) -> None:
        current_node = self.left.next

        while current_node and index > 0:
            current_node = current_node.next
            index -= 1

        if current_node and index == 0:
            new_node = ListNode(val)

            prev_node = current_node.prev

            prev_node.next = new_node
            new_node.prev = prev_node

            current_node.prev = new_node
            new_node.next = current_node

    # TC: O(n)
    # SC: O(1)
    def deleteAtIndex(self, index: int) -> None:
        current_node = self.left.next

        while current_node and index > 0:
            current_node = current_node.next
            index -= 1

        if current_node and current_node != self.right and index == 0:
            prev_node = current_node.prev
            next_node = current_node.next

            prev_node.next = next_node
            next_node.prev = prev_node


lt = MyLinkedList()
lt.addAtHead(7)
lt.addAtHead(2)
lt.addAtHead(1)
lt.addAtIndex(3, 0)
lt.deleteAtIndex(2)
lt.addAtHead(6)
lt.addAtTail(4)
lt.get(4)
lt.addAtHead(4)
lt.addAtIndex(5, 0)
lt.addAtHead(6)

left = lt.left
right = lt.right


def traverse(left, right):
    current_head = left.next

    while current_head and current_head != right:
        current_head = current_head.next


traverse(left, right)
