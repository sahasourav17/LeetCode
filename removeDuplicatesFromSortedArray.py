class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
            Set for finding the unique elements
            and then this set is converted into a list
            finally, I've sorted them as the result should be
            in a sorted format.
        '''
        set_nums = list(set(nums))
        set_nums.sort()
        k = len(set_nums)

        '''
            Here,I've looped through only k times
            because it doesn't matter what we leave beyond the 
            returned k.
        '''
        for i in range(k):
            nums[i] = set_nums[i]
        return k
