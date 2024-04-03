import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = nums1 + nums2
        a = np.array(l)
        return np.median(a)
    

arr = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8, 9, 10]
sol = Solution().findMedianSortedArrays(arr, arr2)
print(sol)