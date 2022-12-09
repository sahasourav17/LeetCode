class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        sorted_dict = sorted(d.items(), key=lambda x:x[1],reverse =True)

        s = ""
        for item,val in sorted_dict:
            # print(item,val)
            while val>0:
                s += item
                val -= 1
        return s

