class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        list1 = []
        l1 = [1]
        list1.append(l1)
        if rowIndex == 0:
            return list1[-1]
        l2 = [1, 1]
        list1.append(l2)
        for i in range(2, rowIndex + 1):
            l = [1]
            for j in range(1, i):
                l.append(list1[i - 1][j - 1] + list1[i - 1][j])
            l.append(1)
            list1.append(l)

        return list1[-1]


print(Solution().getRow(3))
print(Solution().getRow(33))