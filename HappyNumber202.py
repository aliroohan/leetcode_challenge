class Solution:
    def isHappy(self, n: int) -> bool:
        number = str(n)
        while len(number) != 1:
            sum = 0
            for i in number:
                sum += int(i) ** 2

            number = str(sum)

        if number == '1' or number == '7':
            return True
        else:
            return False


print(Solution().isHappy(19))
print(Solution().isHappy(2))
print(Solution().isHappy(7))