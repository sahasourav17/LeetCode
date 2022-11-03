class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        oldColor = image[sr][sc]

        '''
        I've implemented this using FloodFill Algorithm which I've learnt
        in Computer Graphics Course.

        '''
        def floodAlgo(i,j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if image[i][j] == color: 
                return
            if image[i][j] != oldColor:
                return
            image[i][j] = color

            floodAlgo(i,j+1)
            floodAlgo(i,j-1)
            floodAlgo(i+1,j)
            floodAlgo(i-1,j)

        floodAlgo(sr,sc)

        return image
