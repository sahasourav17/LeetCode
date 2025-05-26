class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)

        low, high = 0, n - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == mid:
                low = mid + 1
            else:
                high = mid - 1
        return low
