class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""
        for i in range(len(s)):
            if ("A" <= s[i] <= "Z") or ("a" <= s[i] <= "z"):
                a += s[i].lower()
            elif "0" <= s[i] <= "9":
                a += s[i]

        for i in range(len(a) // 2):
            if a[i] != a[len(a) - i - 1]:
                return False

        return True

s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))
