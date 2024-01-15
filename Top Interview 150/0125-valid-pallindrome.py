class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = list(map(str.lower,filter(str.isalnum,s)))
        return l == l[::-1]
        
