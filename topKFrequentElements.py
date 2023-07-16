class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        res = []
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        sortedDict = dict(sorted(d.items(), key = lambda x: x[1], reverse = True))
        for i,(key,value) in enumerate(sortedDict.items()):
            if len(res) < k:
                res.append(key)
        return res 