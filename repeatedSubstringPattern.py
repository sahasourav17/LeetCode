# Approach 1
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sLength = len(s)
        for i in range(1, sLength//2+1):
            subStr = s[:i]
            if sLength % i == 0 and subStr*(sLength // i) == s:
                return True

        return False

# Time Complexity : O(N^2)
# Space Complexity : o(N)


# Approach 2

"""
    step 1: concatenate the same string twice
    step 2: remove first and last character
    step 3: check if original string is present in the string obtained from step 2
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]

# Time Complexity: O(N)
# Space Complexity: O(N)
