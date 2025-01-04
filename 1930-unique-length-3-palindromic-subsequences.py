class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = {}
        for i in s:
            right[i] = right.get(i, 0) + 1
        
        for m in s:
            right[m] -= 1
          
            for c in left:
                if right[c] > 0:
                    res.add((m,c))
            left.add(m)

        return len(res)

        

# More Efficient Approach
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        n = len(s)
        
        # Precompute the first and last occurrence of each character
        first = {}
        last = {}
        
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
        
        # Iterate over each unique character
        for c in set(s):
            if first[c] < last[c]:
                # Find all unique characters between the first and last occurrence of `c`
                unique_middle = set(s[first[c] + 1:last[c]])
                for m in unique_middle:
                    res.add((c, m))
        
        return len(res)
