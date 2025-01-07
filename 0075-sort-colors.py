# Bucket sort (Trivial Solution)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1

        idx = 0
        for color in range(3):
            cnt = d.get(color, 0)
            nums[idx : idx + cnt] = [color] * cnt
            idx += cnt

