import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1:
            if n % 2 == 0:
                n /= 2
            else:
                return False

        return True

    def isPowerOfTwoAlternate(self, n: int) -> bool:
        if n <= 0:
            return False
        if math.log2(n) % 1 == 0:
            return True
        else:
            return False


print(Solution().isPowerOfTwo(16))
print(Solution().isPowerOfTwo(218))
print(Solution().isPowerOfTwoAlternate(16))
print(Solution().isPowerOfTwoAlternate(218))
