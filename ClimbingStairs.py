class Solution:
    def climbStairs(self, n: int) -> int:
        table = {}
        def calcSteps(n,table):
            # base case
            if n < 2: return 1
            if not n in table:
                table[n] = calcSteps(n-1,table)+calcSteps(n-2,table)
            return table[n]

        return calcSteps(n,table)