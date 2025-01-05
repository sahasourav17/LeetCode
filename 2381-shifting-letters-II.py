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

