class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden, lower, upper = set(forbidden), 0, 1e6
        if 0 in forbidden:
            return -1
        queue, steps = deque(), -1
        queue.append((0, True))
        forbidden.add(0)
        while queue:
            steps += 1            
            for i in range(len(queue)):
                pos, canBackwards = queue.popleft()                
                if pos == x:
                    return steps                
                if (canBackwards and pos - b > 0 and pos-b not in forbidden):
                    queue.append((pos-b, False))
                    forbidden.add(pos-b)                
                if (pos+a <= upper and pos+a not in forbidden):
                    queue.append((pos+a, True))
                    forbidden.add(pos+a)        
        return -1
