class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = 0
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i] >= goal:
                goal = i
        # if goal = 0 that means we can reach to the goal otherwise not
        return goal == 0
# Time Complexity: O(n)
