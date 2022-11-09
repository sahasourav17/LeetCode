from collections import Counter
class Solution:
    def equalFrequency(self, word: str) -> bool:
        # print(d)
        for i in range(len(word)):
            newStr = word[:i]+word[i+1:]
            # print(newStr)
            if len(set(Counter(newStr).values())) == 1:
                # print(Counter(newStr))
                return True
        return False
