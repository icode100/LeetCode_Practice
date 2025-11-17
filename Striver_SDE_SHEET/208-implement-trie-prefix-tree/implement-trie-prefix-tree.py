class Node:
    def __init__(self):
        self.hashmap = dict()
        self.flag = False
    def insert(self,c):
        if c in self.hashmap: return self.hashmap[c]
        self.hashmap[c]=Node()
        return self.hashmap[c]
    def contains(self,c):
        if c in self.hashmap: return self.hashmap[c]
        return None
class Trie:

    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        ptr = self.root
        for c in word:
            node = ptr.insert(c)
            ptr = node
        ptr.flag = True
        

    def search(self, word: str) -> bool:
        ptr = self.root
        for c in word:
            if ptr: ptr = ptr.contains(c)
            else: return False
        if not ptr: return False
        return ptr.flag

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for c in prefix:
            if ptr: ptr = ptr.contains(c)
            else: return False
        if not ptr: return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)