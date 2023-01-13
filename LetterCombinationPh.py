class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = []

        """
            1. Give a digit sequence 
            2. if digit sequence is empty 
                add the current to the result list
            3. else generate combination of remaining letters
        """

        def dfs(digitSeq,current):
            if not digitSeq:
                result.append(current)
                return
            for letter in digitMap[digitSeq[0]]:
                dfs(digitSeq[1:],current+letter)
         
        dfs(digits,"")
        return result