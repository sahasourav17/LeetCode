class Solution:
    def vowelStrings(self, words, queries):
        prefix = []
        res = []
        count = 0

        def isVowel(c):
            return c in 'aeiou'

        for word in words:
            if isVowel(word[0]) and isVowel(word[-1]):
                count += 1
            prefix.append(count)

        for l, r in queries:
            if l == 0:
                res.append(prefix[r])
            else:
                res.append(prefix[r] - prefix[l - 1])

        return res
