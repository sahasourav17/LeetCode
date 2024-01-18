class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sLen = len(s)
        tLen = len(t)
        if sLen > tLen:
            return False
        if sLen == 0:
            return True
        subSequence = 0
        for i in range(tLen):
            if subSequence <= sLen-1 and  s[subSequence] == t[i]:
                subSequence += 1
        return subSequence == sLen
