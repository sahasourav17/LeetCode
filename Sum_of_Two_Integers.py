# TLE using half adder idea in input(-1,1)
# def Add(x,y):
#     while(y!=0):
#         carry = x&y
#         print(f'before shift : {carry}')
#         x = x ^ y
#         y = carry << 1
#         print(f'after shift : {y}')
#     return x
# print(Add(2,3))

import math


class Solution:
    def getSum(self, a: int, b: int) -> int:
        n = (2**a)*(2**b)
        return int(math.log(n,2))
obj = Solution()
print(obj.getSum(-1,1))