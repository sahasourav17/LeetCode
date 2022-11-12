class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = len(nums)
        prefixSum,suffixSum = [0]*l,[0]*l
        prefixSum[0],suffixSum[l-1] = nums[0],nums[l-1]

        for i in range(1,l):
            prefixSum[i] = prefixSum[i-1]+nums[i]
            print(prefixSum[i])

        for i in range(l-2,-1,-1):
            suffixSum[i] = suffixSum[i+1]+nums[i]

        for i in range(l):
            if prefixSum[i] == suffixSum[i]:
                return i
        return -1