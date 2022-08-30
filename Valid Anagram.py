class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq1,freq2 = {},{}
        for ch in s:
            if ch in freq1:
                freq1[ch] += 1
            else:
                freq1[ch] = 1
        for ch in t:
            if ch in freq2:
                freq2[ch] += 1
            else:
                freq2[ch] = 1

        for key in freq2:
            if key not in freq1 or freq1[key] != freq2[key]:
                return False
        return True