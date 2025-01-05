# Trivial Solution (GOT TLE on test case 32)
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = [ord(c) - ord("a") for c in s]

        for start, end, d in shifts:
            for i in range(start, end + 1):
                s[i] += 1 if d else -1
                s[i] = s[i] % 26

        s = [chr(ord("a") + n) for n in s]

        return "".join(s)


## Efficient Solution ( Prefix Sum)
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix_diff = [0] * (n + 1)

        for left, right, d in shifts:
            prefix_diff[right+1] += 1 if d else -1
            prefix_diff[left] += -1 if d else 1

        diff = 0
        res = [ord(c) - ord("a") for c in s]

        for i in reversed(range(n + 1)):
            diff += prefix_diff[i]
            res[i - 1] = (diff + res[i - 1]) % 26

        s = [chr(ord("a") + n) for n in res]

        return "".join(s)


