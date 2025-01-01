## Initial 
class Solution:
    def maxScore(self, s: str) -> int:
        score = 0
        for i in range(len(s)-1):
            left_score = s[:i+1].count('0')
            right_score = s[i+1:].count('1')

            score = max(score, left_score + right_score)
        return score


## refactored version
class Solution:
    def maxScore(self, s: str) -> int:
        zero = 0
        one = s.count("1")
        score = 0

        for i in range(len(s) - 1):
            if s[i] == "0":
                zero += 1
            else:
                one -= 1

            score = max(score, zero + one)

        return score
