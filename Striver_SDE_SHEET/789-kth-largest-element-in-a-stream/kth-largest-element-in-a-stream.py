class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.container = SortedList()
        for n in nums: self.container.add(n)
        self.k = k

    def add(self, val: int) -> int:
        self.container.add(val)
        return self.container[-self.k]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)