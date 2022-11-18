class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low,high = 0,len(nums)-1

        while low <= high:

            mid = low + (high - low)//2

            # found the target and return the index
            if nums[mid] == target:
                return mid

            # search in left half
            elif nums[mid] < target:
                low = mid + 1
            # search in right half
            else:
                high = mid - 1

        return -1