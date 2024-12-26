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


# Dynamic Programming
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]

        # (0 elements, 0 Sum) -> 1 way
        # 1 way to sum to 0 with first 0 elements
        dp[0][0] = 1

        for i in range(len(nums)):
            for cur_sum, count in dp[i].items():
                dp[i + 1][cur_sum + nums[i]] += count
                dp[i + 1][cur_sum - nums[i]] += count
            # print(f"{i} -> {dp[i].items()}")
        return dp[len(nums)][target]
