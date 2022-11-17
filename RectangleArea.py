class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        '''
            case-1: if two rectangles doesn't overlap
                Then we will return the sum of two rectangles area

            case-2: if overlap
                return sum of two rectangle area - overlapped area
        '''

        totalArea = (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1)

        # Case 1
        if ax2 <= bx1 or ay1 >= by2 or ax1 >= bx2 or ay2 <= by1:
            return totalArea

        # Case 2
        overlapArea = (min(ax2, bx2) - max(ax1, bx1))*(min(ay2, by2) - max(ay1, by1))

        return totalArea - overlapArea
