class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = {}
        ans = 0
        for i in jewels:
            d[i] = 1
        for i in stones:
            if i in d:
                ans += 1
        return ans