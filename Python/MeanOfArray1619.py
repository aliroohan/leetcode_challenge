class Solution:
    def trimMean(self, arr: list[int]) -> float:
        n = len(arr)
        no_of_digits = n // 20
        for i in range(no_of_digits):
            a = arr.index(max(arr))
            arr.pop(a)
            b = arr.index(min(arr))
            arr.pop(b)
        
        sum = 0
        for i in range(len(arr)):
            sum += arr[i]

        return sum / len(arr)
        
        

solution = Solution()
arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
result = solution.trimMean(arr)
print(result)