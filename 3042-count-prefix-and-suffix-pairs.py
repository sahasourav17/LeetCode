class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        cnt = 0
        for i in range(len(words)):
            word = words[i]
            for j in range(i+1, len(words)):
                if words[j].startswith(word) and words[j].endswith(word):
                    cnt += 1
        return cnt
