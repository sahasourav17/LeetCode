class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        sortedDict = sorted(d.items(), key=lambda x: x[1], reverse=True)
        return sortedDict[0][0]
