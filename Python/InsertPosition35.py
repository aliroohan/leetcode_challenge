class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        else:
            return len(nums)



print(Solution().searchInsert([1,3,5,6], 5))