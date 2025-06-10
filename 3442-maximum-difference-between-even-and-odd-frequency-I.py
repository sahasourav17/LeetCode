class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        max_odd, min_even = 0, len(s)

        for f in freq.values():
            if f == 0:
                continue
            if f & 1:
                max_odd = max(f, max_odd)
            else:
                min_even = min(f, min_even)

        return max_odd - min_even
