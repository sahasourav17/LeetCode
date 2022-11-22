class Solution:
    def fib(self, n: int) -> int:

        def fibonacci(n,table):
            if n < 2:
                return n

            if not n in table:
                table[n] = fibonacci(n-1,table)+fibonacci(n-2,table)
            return table[n]
        table = {}
        return fibonacci(n,table)