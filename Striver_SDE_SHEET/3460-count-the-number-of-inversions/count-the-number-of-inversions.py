from typing import List
MOD = 10**9 + 7

class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        # build map: prefix length k -> required sum S (prefix length = end+1)
        req_map = {0: 0}  # prefix length 0 has sum 0
        for end, cnt in requirements:
            k = end + 1
            if k in req_map and req_map[k] != cnt:
                return 0
            req_map[k] = cnt

        # sort by prefix length
        items = sorted(req_map.items())  # list of (k, S)
        # sanity checks: nondecreasing sums and sums in feasible range
        prev_k, prev_S = items[0]
        if prev_k != 0 or prev_S != 0:
            return 0
        for k, S in items[1:]:
            if S < prev_S:
                return 0
            if S < 0 or S > k*(k-1)//2:
                return 0
            prev_k, prev_S = k, S

        # we'll step through successive constraints; include final boundary at n if not present
        if n not in req_map:
            items.append((n, None))  # placeholder, meaning "no fixed sum at n" (free tail)
        else:
            # final fixed at n is present; okay
            pass

        total_ways = 1
        prev_k, prev_S = 0, 0

        # iteratively handle each block between prev_k and k
        for k, S in items[1:]:
            L = prev_k
            R = k  # block indices L .. R-1
            bounds = list(range(L, R))  # for index i, bound = i
            max_possible = sum(bounds)
            # target sum for this block:
            if S is None:
                # tail block: no fixed target, we need sum over all possible sums
                target = max_possible
                need_exact = False
            else:
                target = S - prev_S
                need_exact = True
                if target < 0 or target > max_possible:
                    return 0

            # dp[s] = number ways to get sum s using processed elements of this block
            # initialize dp = [1] (zero elements)
            dp = [1] + [0] * target

            # for each bound u, convolve dp with (1 + x + ... + x^u)
            for u in bounds:
                # new_dp[s] = sum_{t=0..min(s,u)} dp[s-t]
                # compute prefix sums of dp for O(target)
                pref = [0] * (target + 1)
                running = 0
                for i in range(target + 1):
                    running = (running + dp[i]) % MOD
                    pref[i] = running
                new_dp = [0] * (target + 1)
                for s in range(target + 1):
                    left = s - u - 1
                    if left >= 0:
                        val = (pref[s] - pref[left]) % MOD
                    else:
                        val = pref[s] % MOD
                    new_dp[s] = val
                dp = new_dp

            if need_exact:
                ways_block = dp[target]  # coefficient of x^{target}
            else:
                # tail block: sum all dp[s] for s=0..target
                ways_block = sum(dp) % MOD

            total_ways = (total_ways * ways_block) % MOD
            prev_k = k
            prev_S = S if S is not None else prev_S  # if tail had no S, prev_S unchanged

        return total_ways % MOD