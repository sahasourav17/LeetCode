class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        common_element = set(nums1) & set(nums2)
        if common_element:
            return min(common_element)
        return -1
