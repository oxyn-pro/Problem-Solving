class ListNode:
    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:

    def __init__(self):
        self.capacity = 1000
        self.map = [ListNode() for i in range(self.capacity)]

    # TC: O(n), but on average it is O(1)
    # SC:  O(m), where  m  is the table’s capacity.

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        cur_node = self.map[index]

        while cur_node.next != None:
            cur_node = cur_node.next
            if cur_node.key == key:
                cur_node.value = value
                return

        new_node = ListNode(key, value)
        cur_node.next = new_node

    def get(self, key: int) -> int:
        index = self._hash(key)
        cur_node = self.map[index]

        while cur_node.next != None:
            cur_node = cur_node.next
            if cur_node.key == key:
                return cur_node.value

        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        cur_node = self.map[index]

        while cur_node.next != None:
            if cur_node.next.key == key:
                cur_node.next = cur_node.next.next
                return
            cur_node = cur_node.next

    def _hash(self, key):
        return key % self.capacity


obj = MyHashMap()
obj.put(1, 1)
obj.put(2, 2)
obj.get(1)
obj.get(3)
obj.put(2, 1)
obj.get(2)
obj.remove(2)
obj.get(2)
