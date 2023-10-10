# Approach 1


class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = pow(2, 31) - 1
        INT_MIN = pow(-2, 31)

        sign = -1 if x < 0 else 1
        ans = 0
        x = abs(x)

        while x != 0:
            ans = ans * 10 + x % 10
            x //= 10
        ans *= sign

        if ans > INT_MAX or ans < INT_MIN:
            return 0
        return ans


# Approach 2


class Solution:
    def reverse(self, x: int) -> int:
        flag = -1 if x < 0 else 1

        s = str(abs(x))
        x = int(s[::-1])

        return x * flag if x < 2**31 else 0
