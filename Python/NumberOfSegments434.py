class Solution:
    def countSegments(self, s: str) -> int:
        l = s.split(" ")
        i = 0
        while i < len(l):
            if l[i] == "":
                l.pop(i)
                i -= 1

            i += 1

        return len(l)


print(Solution().countSegments("Hello, my name is John"))
print(Solution().countSegments("                "))
print(Solution().countSegments("                a"))