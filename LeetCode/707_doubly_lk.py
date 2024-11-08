class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:
    """Doubly Linked list"""

    def __init__(self):
        self.head = None
        self.tail = None

    # TC: O(n)
    # SC: O(1)
    def get(self, index: int) -> int:
        if not self.head:
            return -1

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

        if not self.head:
            self.head = new_node
            self.tail = new_node

        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    # TC: O(1)
    # SC: O(1)
    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)

        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # TC: O(n)
    # SC: O(1)
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        new_node = ListNode(val)
        current_node = self.head
        curr_idx = 0

        while current_node and curr_idx < index:
            current_node = current_node.next
            curr_idx += 1

        if curr_idx == index:
            if current_node is None:
                self.addAtTail(val)
            else:
                prev_node = current_node.prev
                prev_node.next = new_node
                new_node.prev = prev_node
                new_node.next = current_node
                current_node.prev = new_node

    # TC: O(n)
    # SC: O(1)
    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return

        if index == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                next_head = self.head.next
                next_head.prev = None
                self.head = next_head
            return

        current_node = self.head
        curr_idx = 0
        while current_node:
            if curr_idx == index:
                if current_node == self.tail:
                    prev_node = current_node.prev
                    prev_node.next = None
                    self.tail = prev_node
                else:
                    prev_node = current_node.prev
                    next_node = current_node.next
                    prev_node.next = next_node
                    next_node.prev = prev_node
                return

            current_node = current_node.next
            curr_idx += 1


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
    current_head = head

    while current_head:
        current_head = current_head.next


traverse(head)
