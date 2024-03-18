class Solution:
    def reverseString(self, s: list[str]) -> None:
        for i in range(len(s) // 2):
            temp = s[i]
            s[i] = s[len(s) - i - 1]
            s[len(s) - i - 1] = temp


s = ["h","e","l","l","o"]
Solution().reverseString(s)
print(s)