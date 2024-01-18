class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        n = len(s)
        for i in range(n):
            if i < n-1 and values[s[i]] < values[s[i+1]]:
                ans -= values[s[i]]
            else:
                ans += values[s[i]]
        return ans
