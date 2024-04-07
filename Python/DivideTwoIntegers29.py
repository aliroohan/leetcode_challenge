class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if int(dividend/divisor) > 2147483647:
            return 2147483647
        return int(dividend/divisor)
    

print(Solution().divide(10, 3)) # 3
print(Solution().divide(7, -3)) # -2