class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for start in nums:
            if start-1 not in nums_set:
                end = start + 1
                while end in nums_set:
                    end += 1
                res = max(res, end-start)
        return res
