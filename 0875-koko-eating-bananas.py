class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        def canEat(speed):
            hours = 0
            for pile in piles:
                hours += ceil(pile/speed)
            return hours <= h

        while l <= r:
            m = (l + r) // 2
            if canEat(m):
                r = m - 1
            else:
                l = m + 1

        return l
