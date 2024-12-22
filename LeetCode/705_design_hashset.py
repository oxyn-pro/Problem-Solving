class Pair:
    def __init__(self, key):
        self.key = key


class MyHashSetOpen:
    """HashSet using Hashing + Open Addressing"""

    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.map = [None, None]
        self.deleted = Pair(-1)

    # TC: O(n), but on average it is O(1)
    # SC:  O(m), where  m  is the table’s capacity.
    # The amortized time complexity remains  O(1),
    # because the resizing doubles the capacity,
    # and the cost of rehashing is spread across subsequent operations.

    def add(self, key: int) -> None:
        index = self._hash(key)

        while True:
            if self.map[index] is None or self.map[index] == self.deleted:
                self.map[index] = Pair(key)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self._rehash()
                return
            elif self.map[index].key == key:
                return

            index += 1
            index = index % self.capacity

    def remove(self, key: int) -> None:
        index = self._hash(key)

        while self.map[index] != None:
            if self.map[index] != self.deleted and self.map[index].key == key:
                self.map[index] = self.deleted
                self.size -= 1
                return

            index += 1
            index = index % self.capacity

    def contains(self, key: int) -> bool:
        index = self._hash(key)

        while self.map[index] != None:
            if self.map[index] != self.deleted and self.map[index].key == key:
                return True

            index += 1
            index = index % self.capacity
        return False

    def _hash(self, key):
        return key % self.capacity

    def _rehash(self):
        self.capacity = 2 * self.capacity
        new_map = []
        for _ in range(self.capacity):
            new_map.append(None)

        old_map = self.map
        self.map = new_map
        self.size = 0
        for pair in old_map:
            if pair and pair != self.deleted:
                self.add(pair.key)


obj_open = MyHashSetOpen()
obj_open.remove(1)
obj_open.add(9)
obj_open.remove(24)
obj_open.add(53)
obj_open.add(84)
obj_open.remove(90)
obj_open.add(34)
obj_open.contains(9)
obj_open.add(39)
obj_open.contains(84)
obj_open.add(18)
obj_open.contains(9)
obj_open.remove(2)
obj_open.remove(34)
obj_open.contains(18)


class ListNode:
    def __init__(self, key=-1, next=None):
        self.key = key
        self.next = next


class MyHashSetChain:
    """HashSet using Hashing + Chaining"""

    def __init__(self):
        self.capacity = 1000
        self.map = [ListNode() for _ in range(self.capacity)]

    # TC: O(n), but on average it is O(1)
    # SC:  O(m), where  m  is the table’s capacity.

    def add(self, key: int) -> None:
        index = self._hash(key)
        cur_node = self.map[index]

        while cur_node.next:
            cur_node = cur_node.next
            if cur_node.key == key:
                return

        new_node = ListNode(key)
        cur_node.next = new_node

    def remove(self, key: int) -> None:
        index = self._hash(key)
        cur_node = self.map[index]

        while cur_node.next:
            if cur_node.next.key == key:
                cur_node.next = cur_node.next.next
                return
            cur_node = cur_node.next

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        cur_node = self.map[index]

        while cur_node.next:
            cur_node = cur_node.next
            if cur_node.key == key:
                return True
        return False

    def _hash(self, key):
        return key % self.capacity


obj_chain = MyHashSetChain()
obj_chain.remove(1)
obj_chain.add(9)
obj_chain.remove(24)
obj_chain.add(53)
obj_chain.add(84)
obj_chain.remove(90)
obj_chain.add(34)
obj_chain.contains(9)
obj_chain.add(39)
obj_chain.contains(84)
obj_chain.add(18)
obj_chain.contains(9)
obj_chain.remove(2)
obj_chain.remove(34)
obj_chain.contains(18)
