class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hmap = {}
        self.left_node = ListNode()
        self.right_node = ListNode()

        self.left_node.next = self.right_node
        self.right_node.prev = self.left_node

    # TC: O(1)
    # SC: O(1)
    def get(self, key: int) -> int:
        if key in self.hmap:
            node = self.hmap[key]
            self._remove(node)
            self._insert(node)
            return node.val
        return -1

    # TC: O(1)
    # SC: O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self._remove(self.hmap[key])

        new_node = ListNode(key, value)
        self.hmap[key] = new_node
        self._insert(new_node)
        if len(self.hmap) > self.capacity:
            lru = self.left_node.next
            self._remove(lru)
            del self.hmap[lru.key]

    def _insert(self, new_node):
        prev_node = self.right_node.prev

        prev_node.next = new_node
        new_node.prev = prev_node

        new_node.next = self.right_node
        self.right_node.prev = new_node

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node


capacity = 2
obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
obj.put(4, 4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))
