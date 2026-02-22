class Solution:
   def maximumValueSum(self,nums, k, edges):
        base_sum = sum(nums)
        deltas = [(num ^ k) - num for num in nums]

        total_gain = 0
        positive_count = 0
        min_abs_delta = float('inf')

        for d in deltas:
            if d > 0:
                total_gain += d
                positive_count += 1
            min_abs_delta = min(min_abs_delta, abs(d))

        if positive_count % 2 == 0:
            return base_sum + total_gain
        else:
            return base_sum + total_gain - min_abs_delta