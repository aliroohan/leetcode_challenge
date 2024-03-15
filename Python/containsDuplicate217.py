class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)


print(Solution().containsDuplicate([1, 2, 3, 1]))
print(Solution().containsDuplicate([1, 2, 3, 4]))