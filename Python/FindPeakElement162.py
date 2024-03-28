class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = max(nums)
        return nums.index(n)



print(Solution().findPeakElement([1,2,3,1]))