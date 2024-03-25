class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        num = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        list1 = []

        length = len(digits)
        if length == 0:
            return ""
        elif length == 1:
            return num[digits]
        elif length == 2:
            for i in range(len(num[digits[0]])):
                a = ''
                a += num[digits[0]][i]
                for j in range(len(num[digits[1]])):
                    a += num[digits[1]][j]
                    list1.append(a)
                    a = num[digits[0]][i]

            return list1

        elif length == 3:
            for i in range(len(num[digits[0]])):
                a = ''
                temp = num[digits[0]][i]
                for j in range(len(num[digits[1]])):
                    temp1 = num[digits[1]][j]
                    for k in range(len(num[digits[2]])):
                        a = temp + temp1 + num[digits[2]][k]
                        list1.append(a)

                    a = ''
            return list1

        else:
            for i in range(len(num[digits[0]])):
                a = ''
                temp = num[digits[0]][i]
                for j in range(len(num[digits[1]])):
                    temp1 = num[digits[1]][j]
                    for k in range(len(num[digits[2]])):
                        temp2 = num[digits[2]][k]
                        for l in range(len(num[digits[3]])):
                            a = temp + temp1 + temp2 + num[digits[3]][l]
                            list1.append(a)

                    a = ''
            return list1


print(Solution().letterCombinations("23"))
print(Solution().letterCombinations("234"))
print(Solution().letterCombinations("2345"))