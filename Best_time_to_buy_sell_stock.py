class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,profit = 0,0
        for r in range(1,len(prices)):
            cur_profit = prices[r]-prices[l]
            if prices[l]<prices[r]:
                profit = max(cur_profit,profit)
            else:
                l = r
        return profit