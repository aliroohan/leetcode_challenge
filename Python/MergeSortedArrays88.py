class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = m
        while i != len(nums1):
            nums1.pop(i)
        nums1 += nums2
        nums1.sort()



a = [1,2,3,0,0,0]
b = [2,5,6]
Solution().merge(a, 3, b, 3)
print(a)