from collections import defaultdict
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        
        def solve(edges):
            graph = defaultdict(list)
            n = len(edges) + 1
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)

            # Subtree DP
            even = [1] * n   # count itself
            odd = [0] * n

            def dfs1(u, parent):
                for v in graph[u]:
                    if v == parent:
                        continue
                    dfs1(v, u)
                    even[u] += odd[v]
                    odd[u] += even[v]

            dfs1(0, -1)

            # Reroot DP
            new_even = [0] * n
            new_odd = [0] * n

            new_even[0] = even[0]
            new_odd[0] = odd[0]

            def dfs2(u, parent):
                for v in graph[u]:
                    if v == parent:
                        continue

                    # Remove v subtree contribution from u
                    even_out = new_even[u] - odd[v]
                    odd_out  = new_odd[u] - even[v]

                    # Flip parity when moving root to v
                    new_even[v] = even[v] + odd_out
                    new_odd[v]  = odd[v] + even_out

                    dfs2(v, u)

            dfs2(0, -1)

            return new_even

        # Solve both trees
        even1 = solve(edges1)
        even2 = solve(edges2)

        best_tree2 = max(even2)

        # For each node in tree1
        result = []
        for val in even1:
            result.append(val + best_tree2)

        return result