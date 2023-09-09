class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        left = 0
        subStr = set()

        for right in range(len(s)):
            while s[right] in subStr:
                subStr.remove(s[left])
                left += 1
            subStr.add(s[right])
            result = max(result, right - left + 1)
        return result
