class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in nums:
            if (num-1) not in numSet:
                foundlength = 0
                while (num + foundlength) in numSet:
                    foundlength += 1
                longest = max(foundlength,longest)
        return longest
            