class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
            Two pointer approach
            - Time Complexity : O(N)
            - Space Complexity : O(1)
        """
        i,j = 0,len(height)-1
        maxArea = 0
        while i < j:
            if height[i] <= height[j]:
                maxArea = max(height[i]*(j-i),maxArea)
                i += 1
            else:
                maxArea = max(height[j]*(j-i),maxArea)
                j -= 1
        return maxArea
            