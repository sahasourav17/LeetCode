"""
To solve the problem efficiently, we need to analyze the XOR operation properties and leverage mathematical patterns. Specifically:

XOR is commutative and associative, meaning the order of operations doesn't matter.
Any number XORed with itself results in 0.
For every even occurrence, the XOR cancels out (e.g., ( x \oplus x = 0 )).
Given these properties, the XOR of all pairings can be simplified:

If the length of one array is even, all XOR contributions from that array cancel out.
If the length is odd, only the XOR of the elements of the other array matters.
"""


class Solution:
    def xorAllNums(self, nums1, nums2):
        c1 = len(nums1)
        c2 = len(nums2)
        x1 = 0
        x2 = 0
        if c1 % 2 != 0:
            for i in nums2:
                x2 ^= i
        if c2 % 2 != 0:
            for i in nums1:
                x1 ^= i
        return x1 ^ x2
