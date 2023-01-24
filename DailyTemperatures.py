class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]: 
        n = len(temperatures)
        answer = [0]*n
        for i in range(n-1,-1,-1):
            currTemp = temperatures[i]
            dayCount = 0

            j = i + 1
            while j < n:
                if currTemp < temperatures[j]:
                    dayCount = j-i
                    # print(i,j,dayCount)
                    break
                if answer[j] == 0: 
                    break
                j += answer[j]
            answer[i] = dayCount
        return answer