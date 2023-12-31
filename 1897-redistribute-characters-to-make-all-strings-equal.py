class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = {}
        for word in words:
            for char in word:
                counts[char] = counts.get(char,0)+1
        n = len(words)
        for key,val in counts.items():
            if val % n != 0:
                return False
        return True
