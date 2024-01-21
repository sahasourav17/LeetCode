class Solution:
    def rob(self, nums: list[int]) -> int:
        memo = [0]*(len(nums))
        memo[0]=nums[0]
        if len(nums)>1:
            memo[1]=max(nums[1],nums[0])
        for i in range(2,len(nums)):
            memo[i]=max(nums[i]+memo[i-2],memo[i-1])
        return memo[len(nums)-1]
