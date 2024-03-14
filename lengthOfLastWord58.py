class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(" ")[-1])


s = "Hello World"
print(Solution().lengthOfLastWord(s))
s1 = "   fly me   to   the moon  "
print(Solution().lengthOfLastWord(s1))
