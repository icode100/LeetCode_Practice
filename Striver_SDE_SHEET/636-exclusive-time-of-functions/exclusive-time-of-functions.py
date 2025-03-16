from typing import List
from collections import deque

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        run_stack = []  # Stack to track running functions
        wait_queue = deque()  # Queue for waiting functions
        ans = [0] * n  # Store exclusive times
        logs = [(int(x.split(':')[0]), x.split(':')[1], int(x.split(':')[2])) for x in logs]

        for fid, op, time in logs:
            if op == "start":
                if run_stack:
                    # Update the currently running function's time
                    cid, cst = run_stack[-1]
                    ans[cid] += time - cst
                    # Move it to wait queue since it's being paused
                    wait_queue.append((cid, time))
                
                # Push new function onto the stack
                run_stack.append([fid, time])
            else:
                # Function is ending, update its execution time
                cid, cst = run_stack.pop()
                ans[cid] += time - cst + 1

                # Resume the previous function if available
                if wait_queue:
                    prev_fid, _ = wait_queue.pop()
                    run_stack.append([prev_fid, time + 1])

        return ans
