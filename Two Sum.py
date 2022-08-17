# nums = [2,7,11,15]
# target = 9

# d = {}
# for i in range(len(nums)):
#     temp = target-nums[i]
#     if temp in d:
#         print([d[temp],i])
#     d[nums[i]] = i

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            temp = target-nums[i]
            if temp in d:
                return  [d[temp],i]
            d[nums[i]] = i
    
