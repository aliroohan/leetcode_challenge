class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        l = []
        for i in range(1, n + 1):
            if (i % 3 == 0) and (i % 5 == 0):
                temp = "FizzBuzz"
            elif i % 3 == 0:
                temp = "Fizz"
            elif i % 5 == 0:
                temp = "Buzz"
            else:
                temp = f"{i}"
            l.append(temp)

        return l


print(Solution().fizzBuzz(15))