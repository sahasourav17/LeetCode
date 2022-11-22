class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        '''
            if two strings are already equal
        '''
        if s1 == s2:
            return True

        '''
            Counting number of occurance for each character
            in each string.Finally if the two dictionary
            is not equal return False
        '''
        d1,d2 = {},{}

        for i in s1:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1

        for i in s2:
            if i not in d2:
                d2[i] = 1
            else:
                d2[i] += 1

        if d1 != d2:
            return False
        '''
            Calculating number of mismatch
            in two strings.
            If mismatch > 2:
                it isn't possible to make two strings equal
                using one swap.So, return False
        '''
        mismatch = 0
        for i,j in zip(s1,s2):
            if i != j:
                mismatch += 1

                if mismatch > 2:
                    return False
        return True
