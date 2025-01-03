class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums) 
        l_sum = 0  
        cnt = 0 
        for i in range(len(nums) - 1):
            l_sum += nums[i]
            r_sum = total_sum - l_sum

            if l_sum >= r_sum:
                cnt += 1

        return cnt
