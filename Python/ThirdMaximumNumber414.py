class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        se = set(nums)
        l = list(se)
        if len(l) < 3:
            return max(l)
        a = max(l)
        l.remove(a)
        a = max(l)
        l.remove(a)
        return max(l)


print(Solution().thirdMax([3, 2, 1]))
print(Solution().thirdMax([1, 2]))
print(Solution().thirdMax([2, 2, 3, 1]))