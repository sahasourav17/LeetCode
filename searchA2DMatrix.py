class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        l, r = 0, n*m-1
        while l <= r:
            mid = (l+r)//2
            num = matrix[mid // m][mid % m]
            # print(f"mid->{mid}: l-> {l}: r->{r}: num->{num}")
            if num == target:
                return True
            elif num < target:
                l = mid+1
            else:
                r = mid-1
        return False

# Time Complexity: O(log(m*n))
# Space Complexity: O(1)
