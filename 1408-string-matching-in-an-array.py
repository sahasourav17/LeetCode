# Naive approach
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    result.append(words[i])
                    break

        return result

# More concise approach
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        concatenated = " ".join(words)
        
        result = []
        for word in words:
            if concatenated.count(word) > 1:
                result.append(word)
                
        return result
