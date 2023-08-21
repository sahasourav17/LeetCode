class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        subStr = ""
        sLength = len(s)
        for i in range(0, sLength-1):
            subStr += s[i]
            subStrLength = len(subStr)
            if sLength % subStrLength == 0 and subStr*(sLength // subStrLength) == s:
                return True

        return False
