class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sList,tList = [],[]
        for i in s:
            sList.append(s.index(i))
        for i in t:
            tList.append(t.index(i))

        return sList == tList
