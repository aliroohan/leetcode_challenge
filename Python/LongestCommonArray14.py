class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        a = ""

        min_value = len(strs[0])
        
        for i in range(1, len(strs)):
            if len(strs[i]) < min_value:
                min_value = len(strs[i])

        for i in range(min_value):
            for j in range(1, len(strs)):
                if strs[j - 1][i] != strs[j][i]:
                    return a
            a += strs[0][i]

        return a    
                 

a = ["abbb","a","accc","aa"]
print(Solution().longestCommonPrefix(a))