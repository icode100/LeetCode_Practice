class RandomizedSet:

    def __init__(self):
        self.val_to_idx = {}
        self.array = list()

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx: return False
        self.array.append(val)
        self.val_to_idx[val] = len(self.array)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx: return False
        temp = self.val_to_idx[val]
        self.val_to_idx[self.array[-1]] = temp
        self.array[temp],self.array[-1] = self.array[-1],self.array[temp]
        self.array.pop()
        self.val_to_idx.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.array)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()