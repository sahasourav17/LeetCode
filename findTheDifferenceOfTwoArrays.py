class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        setOne, setTwo = set(nums1), set(nums2)
        answer = [list(setOne-setTwo), list(setTwo-setOne)]
        return answer
