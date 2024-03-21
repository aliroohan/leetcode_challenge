class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        sum1 = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            sum1 += nums[i]

        return sum1


print(Solution().arrayPairSum([1, 4, 3, 2]))
print(Solution().arrayPairSum([6, 2, 6, 5, 1, 2]))