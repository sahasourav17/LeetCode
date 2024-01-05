class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            if len(sub) == 0 or sub[-1] < num:
                sub.append(num)
            else:
                idx = self.first(sub, num, len(sub))
                sub[idx] = num
        return len(sub)
    
    # Find the first index of the first element >= num
    def first(self, arr, x, n):
        low = 0
        high = n - 1
        res = -1
        while (low <= high):
            mid = (low + high) // 2
            if arr[mid] < x:
                low = mid + 1
            else:
                res = mid
                high = mid - 1
        return res
