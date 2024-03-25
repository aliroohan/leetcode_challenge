class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))


# Path: Python/MultiplyString43.py

print(Solution().multiply("2", "3"))
print(Solution().multiply("123", "456"))
print(Solution().multiply("123456789", "987654321"))