class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        max_left = values[0]  # This holds the max value of (values[i] + i)

        for j in range(1, len(values)):
            # Calculate the score for the current pair (i, j)
            max_score = max(max_score, max_left + values[j] - j)
            
            # Update max_left to include the current index
            max_left = max(max_left, values[j] + j)

        return max_score
        
