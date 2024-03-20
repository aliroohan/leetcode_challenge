class Solution:
    def triangleType(self, nums: list[int]) -> str:
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        elif nums[0] + nums[2] <= nums[1]:
            return "none"
        elif nums[2] + nums[1] <= nums[0]:
            return "none"
        else:
            if nums[2] == nums[1] == nums[0]:
                return "equilateral"
            elif nums[0] != nums[1] and nums[2] != nums[1] and nums[2] != nums[0]:
                return "scalene"
            else:
                return "isosceles"


print(Solution().triangleType([3,3,3]))
print(Solution().triangleType([3,4,3]))
print(Solution().triangleType([3,4,5]))
print(Solution().triangleType([3,4,7]))