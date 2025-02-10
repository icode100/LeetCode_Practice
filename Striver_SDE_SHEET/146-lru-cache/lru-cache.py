class Node:
    def __init__(self, val=-1, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.start = Node()  
        self.end = Node()    
        self.start.next = self.end
        self.end.prev = self.start
        self.hashmap = {}

    def __len__(self): 
        return len(self.hashmap)

    def __contains__(self, val): 
        return val in self.hashmap

    def append(self, val):
        new_node = Node(val=val, prev=self.end.prev, next=self.end)
        self.end.prev.next = new_node
        self.end.prev = new_node
        self.hashmap[val] = new_node

    def appendleft(self, val):
        new_node = Node(val=val, next=self.start.next, prev=self.start)
        self.start.next.prev = new_node
        self.start.next = new_node
        self.hashmap[val] = new_node

    def pop(self, val):
        if val in self.hashmap:
            node = self.hashmap[val]
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            del self.hashmap[val]

    def popleft(self):
        if len(self.hashmap) == 0:
            return -1
        node = self.start.next
        self.start.next = node.next
        node.next.prev = self.start
        del self.hashmap[node.val]
        return node.val

    def update(self, val):
        self.pop(val)
        self.append(val)


class LRUCache:
    def __init__(self, capacity: int):
        self.list = DoublyLinkedList()
        self.hashmap = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.list:
            self.list.update(key)
            return self.hashmap[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.list:
            self.list.update(key)
        else:
            self.list.append(key)
        self.hashmap[key] = value

        if len(self.list) > self.capacity:
            val = self.list.popleft()
            self.hashmap.pop(val)  # Fixed: Remove the least recently used key
