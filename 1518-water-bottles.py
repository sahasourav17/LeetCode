# Time Complexity: O(N)
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        canDrink = 0
        while numBottles >= numExchange:
            canDrink += numExchange
            numBottles -= numExchange
            numBottles += 1
        return canDrink + numBottles


# Time Complexity: O(1)
"" 
Intution: You can exchange numExchange empty water bottles from the market with one full water bottle. In the other words, 
if you have (numExchange-1) empty water bottles, you can borrow one full water bottle from your friend, and drink it, 
then exchange numExchange empty bottles to one full bottle. Then return it to your friend. Therefore, for every (numExchange-1) empty water bottles, you can gain one free drink!
"""

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles-1)//(numExchange-1)

