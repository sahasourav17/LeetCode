class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = []
        while n>0:
            if n%3 == 0 and n%5 == 0:
                l.append("FizzBuzz")
            elif n%3 == 0:
                l.append("Fizz")
            elif n%5 == 0:
                l.append("Buzz")
            else:
                l.append(str(n))
            n -= 1
        return l[::-1]
