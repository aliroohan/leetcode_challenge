class Solution:
    def convertToBase7(self, num: int) -> str:
        base7 = ""
        if num == 0:
            return "0"
        if num < 0:
            num = -num
            base7 = "-"
        number = ""
        while num >= 1:
            number = number + str(num % 7)
            num //= 7
        base7 += number[::-1]
        return base7


print(Solution().convertToBase7(100))
print(Solution().convertToBase7(-7))