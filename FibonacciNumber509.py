class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return Solution().fib(n-1) + Solution().fib(n-2)


print(Solution().fib(4))
print(Solution().fib(3))