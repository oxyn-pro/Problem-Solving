class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 2 -> 4 -> 3
l1 = ListNode(2)
node_2 = ListNode(4)
node_3 = ListNode(3)

l1.next = node_2
node_2.next = node_3

# 5 -> 6 -> 4
l2 = ListNode(5)
node_4 = ListNode(6)
node_5 = ListNode(4)

l2.next = node_4
node_4.next = node_5


# TC: O(n)
# SC: O(n)
def addTwoNumbers(l1, l2):
    dummy = ListNode()
    cur_node = dummy

    carry = 0
    while l1 or l2 or carry:
        if not l1:
            l1 = ListNode()
        if not l2:
            l2 = ListNode()

        res = l1.val + l2.val + carry

        carry = res // 10
        res = res % 10

        new_node = ListNode(res)
        cur_node.next = new_node

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        cur_node = cur_node.next

    return dummy.next


def traverse(head):
    while head:
        print(head.val)
        head = head.next


head = addTwoNumbers(l1, l2)
traverse(head)
