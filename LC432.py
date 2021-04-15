from collections import defaultdict


class Node(object):
    def __init__(self):
        self.key_set = set([])
        self.prev, self.next = None, None

    def add_key(self, key):
        self.key_set.add(key)

    def remove_key(self, key):
        self.key_set.remove(key)

    def get_any_key(self):
        if self.key_set:
            result = self.key_set.pop()
            self.add_key(result)
            return result
        else:
            return None

    def count(self):
        return len(self.key_set)

    def is_empty(self):
        return len(self.key_set) == 0


class DoubleLinkedList(object):
    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head
        return

    def insert_after(self, x):
        node, temp = Node(), x.next
        x.next, node.prev = node, x
        node.next, temp.prev = temp, node
        return node

    def insert_before(self, x):
        return self.insert_after(x.prev)

    def remove(self, x):
        prev_node = x.prev
        prev_node.next, x.next.prev = x.next, prev_node
        return

    def get_head(self):
        return self.head.next

    def get_tail(self):
        return self.tail.prev

    def get_sentinel_head(self):
        return self.head

    def get_sentinel_tail(self):
        return self.tail


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dll, self.key_counter = DoubleLinkedList(), defaultdict(int)
        self.node_freq = {0: self.dll.get_sentinel_head()}

    def _rmv_key_pf_node(self, pf, key):
        node = self.node_freq[pf]
        node.remove_key(key)
        if node.is_empty():
            self.dll.remove(node)
            self.node_freq.pop(pf)
        return

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        self.key_counter[key] += 1
        cf, pf = self.key_counter[key], self.key_counter[key] - 1
        if cf not in self.node_freq:
            self.node_freq[cf] = self.dll.insert_after(self.node_freq[pf])
        self.node_freq[cf].add_key(key)
        if pf > 0:
            self._rmv_key_pf_node(pf, key)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.key_counter:
            self.key_counter[key] -= 1
            cf, pf = self.key_counter[key], self.key_counter[key] + 1
            if self.key_counter[key] == 0:
                self.key_counter.pop(key)
            if cf != 0:
                if cf not in self.node_freq:
                    self.node_freq[cf] = self.dll.insert_before(self.node_freq[pf])
                self.node_freq[cf].add_key(key)
            self._rmv_key_pf_node(pf, key)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return self.dll.get_tail().get_any_key() if self.dll.get_tail().count() > 0 else ""

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return self.dll.get_head().get_any_key() if self.dll.get_tail().count() > 0 else ""

