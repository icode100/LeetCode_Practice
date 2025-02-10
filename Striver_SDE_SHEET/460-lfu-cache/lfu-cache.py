from collections import defaultdict

class Node:
    def __init__(self, val=-1, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

class DoublyLinkedList:
    def __init__(self):
        self.start = Node()  # Dummy head
        self.end = Node()    # Dummy tail
        self.start.right = self.end
        self.end.left = self.start
        self.hashmap = {}

    def __len__(self):
        return len(self.hashmap)

    def __contains__(self, val):
        return val in self.hashmap

    def append(self, val):
        """ Append at the end (Most Recently Used position) """
        newnode = Node(val=val, left=self.end.left, right=self.end)
        self.hashmap[val] = newnode
        self.end.left.right = newnode
        self.end.left = newnode

    def pop(self, val):
        """ Remove a specific node """
        if val not in self.hashmap:
            return
        node = self.hashmap[val]
        left, right = node.left, node.right
        if left:
            left.right = right
        if right:
            right.left = left
        del self.hashmap[val]

    def pop_lru(self):
        """ Remove the Least Recently Used (LRU) element """
        if len(self.hashmap) == 0:
            return -1
        node = self.start.right  # First real node (skip dummy head)
        if node == self.end:  # No valid node to remove
            return -1
        self.pop(node.val)  # Proper removal
        return node.val

class LFUCache:
    def __init__(self, capacity: int):
        self.checklist = defaultdict(DoublyLinkedList)  # Frequency → DLL
        self.capacity = capacity
        self.hashmap = {}  # key → value
        self.counter = {}  # key → frequency
        self.lf = 0  # Least frequency in cache

    def counter_update(self, key):
        """ Update frequency of a key """
        cnt = self.counter[key]
        self.counter[key] += 1
        self.checklist[cnt].pop(key)
        self.checklist[cnt + 1].append(key)

        if cnt == self.lf and len(self.checklist[cnt]) == 0:
            del self.checklist[cnt]
            self.lf += 1

    def get(self, key: int) -> int:
        """ Fetch a value and update frequency """
        if key in self.hashmap:
            self.counter_update(key)
            return self.hashmap[key]
        return -1

    def put(self, key: int, value: int) -> None:
        """ Insert or update a value and handle eviction if necessary """
        if self.capacity == 0:
            return

        if key in self.hashmap:
            self.hashmap[key] = value
            self.counter_update(key)
            return

        if len(self.hashmap) >= self.capacity:
            if self.lf in self.checklist:  # Ensure self.lf exists
                val = self.checklist[self.lf].pop_lru()
                if val != -1:  # Ensure valid key deletion
                    del self.hashmap[val]
                    del self.counter[val]

        self.hashmap[key] = value
        self.counter[key] = 1
        self.checklist[1].append(key)
        self.lf = 1

# Example Usage
# lfu = LFUCache(2)
# lfu.put(1, 1)
# lfu.put(2, 2)
# print(lfu.get(1))  # Returns 1
# lfu.put(3, 3)      # Evicts key 2
# print(lfu.get(2))  # Returns -1 (not found)
# print(lfu.get(3))  # Returns 3
