class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n):
            if nums[i] != i:
                return i
        else:
            return n


print(Solution().missingNumber([3, 0, 1]))
print(Solution().missingNumber([0, 1]))