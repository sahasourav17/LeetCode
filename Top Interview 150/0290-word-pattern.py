class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordList = s.split()
        if len(pattern) != len(wordList) or len(set(pattern)) != len(set(wordList)):
            return False
        d = {}
        for i in range(len(pattern)):
            if pattern[i] not in d:
                if wordList[i] not in d.values():
                    d[pattern[i]] = wordList[i]
                else:
                    return False
            elif d[pattern[i]] != wordList[i]:
                return False
        return True
