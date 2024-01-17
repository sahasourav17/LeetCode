class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for num in arr:
            d[num] = d.get(num,0)+1
        s = set()
        for val in d.values():
            if val in s:
                return False
            s.add(val)
        return True
