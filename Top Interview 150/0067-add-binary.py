class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a,2)
        b = int(b,2)
        sum = a+b

        if a==0 and b ==0:
            return "0"
        res = ""
        while sum >= 1:
            res += str(int(sum%2))
            sum //= 2
        return res[::-1]
