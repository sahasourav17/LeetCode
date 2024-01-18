class Solution:
    def climbStairs(self, n: int) -> int:
        ways = {
            1:1,
            2:2,
            3:3
        }
        ans = self.findWays(n,ways)
        return ans

    def findWays(self,n,ways):
        if n in ways:
            return ways[n]
        ways[n] =  self.findWays(n-1,ways)+self.findWays(n-2,ways)
        return ways[n]
            
