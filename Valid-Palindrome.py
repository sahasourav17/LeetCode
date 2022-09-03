# def isPalindrome(s):
#     l = []
#     for i in s:
#         if i.isalpha() and i.isalnum() == False:
#             l.append(i.lower())
#         print(l)
#     if l == l[::-1]:
#         return True
#     else:
#         return False


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = list(map(str.lower,filter(str.isalnum,s)))
        return l == l[::-1]

s = input()
obj = Solution()
print(obj.isPalindrome(s))