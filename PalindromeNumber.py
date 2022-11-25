class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = [x for x in str(x)]
        return l[::-1] == l