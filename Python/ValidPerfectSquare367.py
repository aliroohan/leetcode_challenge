import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if math.sqrt(num) % 1 == 0:
            return True
        else:
            return False


print(Solution().isPerfectSquare(16))
print(Solution().isPerfectSquare(14))