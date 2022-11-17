class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        increment = 2*(numRows-1)
        ans = ""
        for row in range(numRows):
            for i in range(row,len(s),increment):
                ans += s[i]

                # Finding jump index in between first and last row
                jumpIndex = i + increment - 2*row
                if row > 0 and row < (numRows-1) and jumpIndex < len(s):
                    ans += s[jumpIndex]
        return ans
