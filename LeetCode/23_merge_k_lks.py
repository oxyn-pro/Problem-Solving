class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(1)
node_2 = ListNode(4)
node_3 = ListNode(5)

head.next = node_2
node_2.next = node_3

head2 = ListNode(1)
node2_2 = ListNode(3)
node2_3 = ListNode(4)

head2.next = node2_2
node2_2.next = node2_3

head3 = ListNode(2)
node3_2 = ListNode(6)

head3.next = node3_2

lists = [head, head2, head3]


# TC: O(n log n)
# SC: O(1)
def mergeKlists(lists):
    if not lists:
        return None

    interval = 1
    ls_length = len(lists)

    # TC: O(log n) because we are incrementing by 2
    while interval < ls_length:
        for i in range(0, ls_length - interval, interval * 2):
            lists[i] = merge(lists[i], lists[i + interval])
        interval *= 2

    return lists[0]


# TC: O(n)
def merge(l1, l2):
    dummy_head = ListNode()
    tail = dummy_head

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    else:
        tail.next = l2

    return dummy_head.next


merged_list = mergeKlists(lists)


# -------- Demonstration --------
def traverse(ls):
    current_head = ls
    while current_head:
        print(current_head.val)
        current_head = current_head.next


traverse(merged_list)
