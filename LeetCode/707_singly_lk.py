class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    """Singly Linked list WITHOUT Dummy Head"""

    def __init__(self):
        self.head = None
        self.tail = None

    # TC: O(n)
    # SC: O(1)
    def get(self, index: int) -> int:
        current_head = self.head
        curr_idx = 0

        while current_head:
            if index == curr_idx:
                return current_head.val
            current_head = current_head.next
            curr_idx += 1
        return -1

    # TC: O(1)
    # SC: O(1)
    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        if self.head.next is None:
            self.tail = self.head

    # TC: O(1)
    # SC: O(1)
    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # TC: O(n)
    # SC: O(1)
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        current_node = self.head
        current_idx = 0

        while current_node and current_idx < index - 1:
            current_node = current_node.next
            current_idx += 1

        if current_node is None:
            return

        new_node = ListNode(val)
        new_node.next = current_node.next
        current_node.next = new_node

        if new_node.next is None:
            self.tail = new_node

        return

    # TC: O(n)
    # SC: O(1)
    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        current_node = self.head
        current_idx = 0

        while current_node:
            if current_idx == index - 1:
                if current_node.next:
                    if current_node.next == self.tail:
                        self.tail = current_node
                    current_node.next = current_node.next.next
                return

            current_node = current_node.next
            current_idx += 1


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

head = lt.head


def traverse(head):
    current = head

    while current:
        current = current.next


traverse(head)
