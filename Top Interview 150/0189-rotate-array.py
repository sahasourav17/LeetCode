# initial approach
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            num = nums.pop()
            nums.insert(0,num)
        
# using list slicing
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        tempArray = nums+nums
        tempArray = tempArray[l-k:l-k+l]
        for i in range(l):
            nums[i] = tempArray[i]
        
# Optimized Code
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverseArray(l,r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        n = len(nums)
        k %= n

        reverseArray(0,n-1) # reverse the whole nums array
        reverseArray(0,k-1) # reverse the first part
        reverseArray(k, n-1) # reverse the last part
        
