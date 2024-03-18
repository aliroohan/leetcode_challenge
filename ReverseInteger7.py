class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            x *= -1
            neg = True
        elif x == 0:
            return 0

        num = str(x)
        y = list(num.strip())
        if len(y) > 1:
            for i in range(len(y) // 2):
                temp = y[i]
                y[i] = y[len(y) - i - 1]
                y[len(y) - i - 1] = temp

        num = "".join(y)
        if int(num) >= 2147483647:
            return 0
        if neg:
            return int(num) * -1
        else:
            return int(num)


    def reverse2(self, x: int) -> int:
        neg = False
        if x < 0:
            x *= -1
            neg = True
        elif x == 0:
            return 0

        num = str(x)

        if int(num[::-1]) >= 2147483647:
            return 0
        if neg:
            return int(num[::-1]) * -1
        else:
            return int(num[::-1])

print(Solution().reverse(123))
print(Solution().reverse(-123))
print(Solution().reverse(120))
print(Solution().reverse(1534236469))
print(Solution().reverse2(-123))
print(Solution().reverse2(120))
print(Solution().reverse2(1534236469))
