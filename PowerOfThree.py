class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def check(x):
            if x == 0: return False
            if x == 1: return True

            if x % 3 == 0:
                return check(x/3)
        return check(n)
