class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        l = [i for i in s]
        n = len(s)//2
        leftHalf,rightHalf = l[:n],l[n:]
        # print(leftHalf,rightHalf)

        leftVowels,rightVowels = 0,0

        for i in leftHalf:
            if i in vowels:
                leftVowels += 1

        for i in rightHalf:
            if i in vowels:
                rightVowels += 1
        return leftVowels == rightVowels
