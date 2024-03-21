class Solution:
    def findLHS(self, nums: list[int]) -> int:
        s = list(set(nums))
        sum = 0
        for i in s:
            if i + 1 in s and nums.count(i) + nums.count(i + 1) > sum:
                sum = nums.count(i) + nums.count(i + 1)

        return sum


print(Solution().findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
print(Solution().findLHS([1, 2, 3, 4]))