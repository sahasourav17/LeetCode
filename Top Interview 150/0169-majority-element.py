# initial approach
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        for num in nums:
            d[num] = d.get(num,0)+1
        for key,val in d.items():
            if val > len(nums)/2:
                return key
# using Boyce-More Voting algorithm
# Time Complexity: O(n) & Space Complexity: O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
