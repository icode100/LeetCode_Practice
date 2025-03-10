"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None:None}
        ptr = head
        while ptr: 
            hashmap[ptr] = Node(ptr.val)
            ptr = ptr.next
        ptr = head
        while ptr: 
            hashmap[ptr].random,hashmap[ptr].next = hashmap[ptr.random],hashmap[ptr.next]
            ptr = ptr.next
        return hashmap[head]
