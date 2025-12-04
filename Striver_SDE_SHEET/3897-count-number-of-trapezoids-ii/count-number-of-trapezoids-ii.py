from typing import List, DefaultDict
from collections import defaultdict
from math import gcd

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # Helper to compute sum of products: Sum(count[i] * count[j]) for i < j
        # This selects one segment from group A and one from group B
        def computeCombinations(groups) -> int:
            total_ans = 0
            for key in groups:
                # Get the counts of segments for each distinct subgroup
                # For lines: subgroup is the specific line intercept
                # For parallelograms: subgroup is the specific slope
                nums = list(groups[key].values())
                
                current_total_segments = sum(nums)
                
                for num in nums:
                    current_total_segments -= num
                    total_ans += (num * current_total_segments)
            return total_ans

        # Data Structures
        # totalLines stores parallel groups.
        # Key: Slope (dy, dx) -> Value: { Line_Identifier : count_of_segments }
        totalLines = defaultdict(lambda: defaultdict(int))

        # parrLines stores segments that share a midpoint.
        # Key: Midpoint (sum_x, sum_y) -> Value: { Slope (dy, dx) : count_of_segments }
        parrLines = defaultdict(lambda: defaultdict(int))

        N = len(points)

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i):
                x2, y2 = points[j]
                
                # 1. Calculate Slope using GCD to avoid float precision issues
                dy = y1 - y2
                dx = x1 - x2
                g = gcd(dy, dx)
                dy //= g
                dx //= g
                
                # Normalize slope direction (so -1/-1 becomes 1/1)
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy
                
                slope_key = (dy, dx)

                # 2. Identify the specific infinite line
                # Equation: dy*x - dx*y = C
                # C is unique for every distinct parallel line
                line_c = dy * x1 - dx * y1
                
                totalLines[slope_key][line_c] += 1

                # 3. Identify Midpoint for Parallelograms
                # We use sum (x1+x2, y1+y2) to represent midpoint (avoiding division/floats)
                mid_key = (x1 + x2, y1 + y2)
                
                parrLines[mid_key][slope_key] += 1

        # Calculate Logic:
        # 1. 'total' calculates all pairs of parallel segments. 
        #    - This counts Trapezoids (1x) and Parallelograms (2x).
        #    (Parallelograms are counted twice because they have 2 pairs of parallel sides).
        # 2. 'parallelograms' calculates distinct parallelograms via shared midpoints.
        # 3. Subtracting counts: (Trapezoids + 2*Parallelograms) - Parallelograms = Total Unique Trapezoids
        
        total = computeCombinations(totalLines)
        parallelograms = computeCombinations(parrLines)

        return total - parallelograms