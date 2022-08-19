from functools import reduce
from turtle import right

# def prodExcept(l):
#     n = len(l)
#     ans = [1 for i in range(n)]
#     for i in range(1,n):
#         ans[i] = ans[i-1]*l[i-1]
#     prod = 1
#     for i in range(n-1,-1,-1):
#         ans[i] *= prod
#         prod *= l[i]
#     return ans

# l = list(map(int,input().split()))
# ans = []
# print(f'Result : {prodExcept(l)}')


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1 for _ in range(n)]
        for i in range(1,n):
            ans[i] = ans[i-1]*nums[i-1]
        prod = 1
        for i in range(n-1,-1,-1):
            ans[i] *= prod
            prod *= nums[i]
        return ans