class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        for i in range(n+1):
            count1 = 0
            # as int contains 32 bits
            for j in range(32):
                bit = (i >> j) & 1
                if bit == 1: count1 += 1
            l.append(count1)
        return l
