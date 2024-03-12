class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[len(digits) - 1] != 9:
            digits[len(digits) - 1] += 1
        else:
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] == 9:
                    digits[i] = 0
                    if digits[0] == 0:
                        digits.insert(0, 1)
                else:
                    digits[i] += 1
                    break

        return digits


print(Solution().plusOne([1, 2, 3]))