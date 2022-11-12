class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open,close,strComb):
            if open == close == n:
                res.append(strComb)
                return
            if open < n:
                backtrack(open+1,close,strComb+"(")
            if close < open:
                backtrack(open,close+1,strComb+")")
        backtrack(0,0,"")

        return res