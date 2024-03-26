class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        a = []
        for i in range(len(matrix)):
            b = []
            for j in range(len(matrix)):
                b.append(matrix[-(j + 1)][i])
            a.append(b)

        for i in range(len(matrix)):
            matrix[i] = a[i]

a = [[1,2,3],[4,5,6],[7,8,9]]
Solution().rotate(a)
print(a)
b = [[5, 1, 9,11],[2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]]
Solution().rotate(b)
print(b)