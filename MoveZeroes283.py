class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0
        ZeroCount = nums.count(0)
        while i < len(nums)-ZeroCount:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                i -= 1
            i += 1



l = [0, 1, 0, 3, 12]
Solution().moveZeroes(l)
print(l)