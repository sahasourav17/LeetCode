class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hashMap = {} # id -> val

        for id, val in nums1:
            hashMap[id] = val
        
        for id, val in nums2:
            hashMap[id] = hashMap.get(id, 0) + val
        
        merged_arr = []
        for k, v in sorted(hashMap.items()):
            merged_arr.append([k,v])
        
        return merged_arr
