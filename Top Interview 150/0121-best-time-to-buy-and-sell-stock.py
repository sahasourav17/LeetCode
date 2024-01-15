# TLE
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        for i in range(n):
            for j in range(i+1,n):
                profit = max((prices[j]-prices[i]),profit)
        return profit

# Greedy Approach O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        left,right = 0,0
        while right < n:
            currentProfit = prices[right]-prices[left]
            if prices[left] < prices[right]:
                profit = max(currentProfit, profit)
            else:
                left = right
            right += 1
        return profit

# Greddy Approach Optimized O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit,left = 0,0
        n = len(prices)
        for i in range(1,n):
            if(prices[i] > prices[left]):
                currentProfit = prices[i]-prices[left]
                maxProfit = max(maxProfit, currentProfit)
            else:
                left = i
        return maxProfit  
