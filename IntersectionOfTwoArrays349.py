class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        l1 = list(s1)
        l2 = list(s2)
        l1.sort()
        l2.sort()
        l = []
        for i in l1:
            if i in l2:
                l.append(i)

        return l



print(Solution().intersection([1,2,2,1], [2,2]))
print(Solution().intersection([4,9,5], [9,4,9,8,4]))