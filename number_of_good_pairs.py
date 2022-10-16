from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        d = defaultdict()
        for i in nums:
            if i in d:
                ans += d[i]
                d[i] += 1
            else:
                d[i] = 1
        return ans