class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory:
    """Doubly Linked list WITH Dummy Heads"""

    def __init__(self, homepage: str):
        self.left = ListNode()
        self.right = ListNode()
        self.current_node = ListNode(homepage)

        self.left.next = self.current_node
        self.current_node.prev = self.left

        self.right.prev = self.current_node
        self.current_node.next = self.right

    # TC: O(1)
    # SC: O(1)
    def visit(self, url: str) -> None:
        new_node = ListNode(url)
        current_node = self.current_node
        right_node = self.right

        current_node.next = new_node
        new_node.prev = current_node

        right_node.prev = new_node
        new_node.next = right_node

        self.current_node = new_node

    # TC: O(n)
    # SC: O(1)
    def back(self, steps: int) -> str:
        current_node = self.current_node

        while current_node.prev != self.left and steps > 0:
            current_node = current_node.prev
            steps -= 1

        self.current_node = current_node
        return self.current_node.val

    # TC: O(n)
    # SC: O(1)
    def forward(self, steps: int) -> str:
        current_node = self.current_node

        while current_node.next != self.right and steps > 0:
            current_node = current_node.next
            steps -= 1

        self.current_node = current_node
        return self.current_node.val


lt = BrowserHistory("leetcode")
lt.visit("google")
lt.visit("facebook")
lt.visit("youtube")
lt.back(1)
lt.back(1)
lt.forward(1)
lt.visit("leetcode")
lt.forward(2)
lt.back(7)

current_node = lt.left


# Just to demonstrate what will look like our linked list at the end.
def traverse(current_node):
    while current_node:
        print(current_node.val)
        current_node = current_node.next


traverse(current_node)
