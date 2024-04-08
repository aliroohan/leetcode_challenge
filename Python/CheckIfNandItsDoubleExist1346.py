class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                if arr.count(0) > 1:
                    return True
                i += 1
                continue
            if arr[i] * 2 in arr:
                return True
            
            i+=1
            

        return False


print(Solution().checkIfExist([10,2,5,3])) # True
print(Solution().checkIfExist([7,1,14,11])) # True
print(Solution().checkIfExist([3,1,7,11])) # False