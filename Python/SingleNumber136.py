class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        a = []
        for i in range(len(nums)):
            if nums[i] not in a:
                a.append(nums[i])
            else:
                a.remove(nums[i])

        return a[0]


print(Solution().singleNumber([2,2,1]))
print(Solution().singleNumber([4,1,2,1,2]))