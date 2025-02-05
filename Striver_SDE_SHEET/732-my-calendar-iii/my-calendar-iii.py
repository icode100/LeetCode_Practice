class SegTree:
    def __init__(self):
        # Key: index of TreeNode
        # Val: max concurrent events for this TreeNode
        self.vals = defaultdict(int)
        # Key: index of TreeNode
        # Val: lazy-counted events for this TreeNode
        self.lazy = defaultdict(int)

    # Pass the current lazy value to children
    def _push(self, v):
        # Pass to left
        self.vals[v * 2] += self.lazy[v]
        self.lazy[v * 2] += self.lazy[v]

        # Pass to right
        self.vals[v * 2 + 1] += self.lazy[v]
        self.lazy[v * 2 + 1] += self.lazy[v]

        # Reset current
        self.lazy[v] = 0

	# Return the max concurrent events in [start, end]
    def query(self, start, end, l=0, r=10**9, v=1) -> int:
        # If [start, end] [l, r] is disjoint
        # Do nothing
        if end < l or r < start:
            return 0
        
        # If [start, end] fully covers [l, r]
        if start <= l <= r <= end:
            return self.vals[v]
        else:
            self._push(v)
            mid = (l + r) // 2
            left = self.query(start, end, l, mid, v * 2)
            right = self.query(start, end, mid + 1, r, v * 2 + 1)
            return max(left, right)

	# Add event [start, end]
    def add(self, start, end, l=0, r=10**9, v=1) -> None:
        # If [start, end] [l, r] is disjoint
        # Do nothing
        if end < l or r < start:
            return
        
        # If [start, end] fully covers [l, r]
        if start <= l <= r <= end:
            self.vals[v] += 1
            self.lazy[v] += 1
        else:
            self._push(v)
            mid = (l + r) // 2
            self.add(start, end, l, mid, v * 2)
            self.add(start, end, mid + 1, r, v * 2 + 1)
            self.vals[v] = max(self.vals[v * 2], self.vals[v * 2 + 1])
class MyCalendarThree:

    def __init__(self):
        self.st = SegTree()

    def book(self, start: int, end: int) -> int:
        end -= 1
        self.st.add(start, end)
        return self.st.query(0, 10**9)


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)