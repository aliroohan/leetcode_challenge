class Solution:
    def addDigits(self, num: int) -> int:
        number = str(num)
        while len(number) != 1:
            sum = 0
            for i in range(len(number)):
                sum += int(number[i])
            number = str(sum)

        return int(number)

print(Solution().addDigits(38))