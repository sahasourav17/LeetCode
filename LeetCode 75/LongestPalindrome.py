class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}
        max = 0
        for i in s:
            if i in letters:
                letters.pop(i)
                max += 2
            else:
                letters[i] = 1

        # print(letters)
        if letters:
            max += 1

        return max