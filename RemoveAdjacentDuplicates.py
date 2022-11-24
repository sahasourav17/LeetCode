class Solution:
    def removeDuplicates(self, s: str) -> str:
        l = []
        for i in range(len(s)):
            if len(l) != 0 and l[-1] == s[i]:
                l.pop()
            else:
                l.append(s[i])
        return "".join(l)