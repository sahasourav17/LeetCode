class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n,m = len(s),len(t)
        i,j = 0,0
        while (i < n and j < m):
            if (s[i] == t[j]):
                i += 1
            j += 1

        '''
            If i reaches end of s,that mean we found all
            characters of s in t,
            so s is subsequence of t, else not
        '''
        return i == n