# Simple Naive Solution 
# TC : O(n^2)

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

#  Monotonic Stack(decreasing order) Solution 
# TC : O(N)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]: 
        n = len(temperatures)
        answer = [0]*n
        stack = []
        
        for idx,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                answer[stack.pop()] = idx - stack[-1]
            stack.append(idx)
        return answer
