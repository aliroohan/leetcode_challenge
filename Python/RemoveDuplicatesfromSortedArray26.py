class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = []
        i = 0
        while i < len(nums):
            if nums[i] not in l:
                l.append(nums[i])
            elif nums[i] in l:
                nums.pop(i)
                i -= 1
            i += 1

        return len(l)


print(Solution().removeDuplicates([1,1,2]))
print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))