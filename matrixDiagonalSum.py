class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        n = len(mat)

        for i in range(n):
            sum += mat[i][i]

        i = 0
        j = n-1

        while i < n and j >= 0:
            #  removing duplicate diagonal elements
            if i != j:
                sum += mat[i][j]
            i += 1
            j -= 1

        return sum

'''
    O(N) solution.
    Best and Efficient solution.
'''

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        n = len(mat)
        j = n-1

        for i in range(n):
            '''
                Adding the value of diagonals
            '''
            sum += mat[i][i] + mat[i][j-i]

        '''
            If the matrix is even square then it has no common diagonal element.
            So, return the sum as it is.
            Else, there is a common diagonal element. So, we need to 
            subtract that element value from sum.
        '''
        return sum if n%2 == 0 else sum - mat[int(j/2)][int(j/2)]