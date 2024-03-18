class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        list1 = []
        l1 = [1]
        list1.append(l1)
        if numRows == 1:
            return list1
        l2 = [1, 1]
        list1.append(l2)
        for i in range(2, numRows):
            l = [1]
            for j in range(1, i):
                l.append(list1[i - 1][j - 1] + list1[i - 1][j])
            l.append(1)
            list1.append(l)

        return list1


print(Solution().generate(5))