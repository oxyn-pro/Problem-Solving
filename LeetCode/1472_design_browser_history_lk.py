class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory:
    """Doubly Linked list WITHOUT Dummy Heads"""

    def __init__(self, homepage: str):
        self.current_node = ListNode(homepage)

    # TC: O(1)
    # SC: O(1)
    def visit(self, url: str) -> None:
        new_node = ListNode(url)
        current_node = self.current_node

        current_node.next = new_node
        new_node.prev = current_node

        self.current_node = new_node

    # TC: O(n)
    # SC: O(1)
    def back(self, steps: int) -> str:
        current_node = self.current_node

        while current_node.prev and steps > 0:
            current_node = current_node.prev
            steps -= 1

        self.current_node = current_node
        return self.current_node.val

    # TC: O(n)
    # SC: O(1)
    def forward(self, steps: int) -> str:
        current_node = self.current_node

        while current_node.next and steps > 0:
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

current_node = lt.current_node


# Just to demonstrate what our linked list will look like at the end.
def retrieve_head(current_node):

    if not current_node.prev:
        return current_node

    while current_node.prev:
        current_node = current_node.prev

    return current_node


head = retrieve_head(current_node)


def traverse(head):
    current_node = head
    while current_node:
        print(current_node.val)
        current_node = current_node.next


traverse(current_node)
