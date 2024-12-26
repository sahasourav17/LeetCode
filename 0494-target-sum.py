class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
       
        dp = {} # (idx, cur_sum) -> no of ways

        def backtrack(i, cur_sum):
            if(i,cur_sum) in dp:
                return dp[(i,cur_sum)]

            if i == len(nums):
                return 1 if cur_sum == target else 0
            
            dp[(i,cur_sum)] = (
                backtrack(i+1, cur_sum + nums[i]) +
                backtrack(i+1, cur_sum - nums[i])
            )

            return dp[(i,cur_sum)]
        
        return backtrack(0,0)
