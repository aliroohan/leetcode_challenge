class Solution:
    def intToRoman(self, num: int) -> str:
        ones = {"1":"I", "2":"II", "3":"III", "4":"IV", "5":"V", "6":"VI", "7":"VII", "8":"VIII", "9":"IX", "0":""}
        tens = {"1":"X", "2":"XX", "3":"XXX", "4":"XL", "5":"L", "6":"LX", "7":"LXX", "8":"LXXX", "9":"XC", "0":""}
        hund = {"1":"C", "2":"CC", "3":"CCC", "4":"CD", "5":"D", "6":"DC", "7":"DCC", "8":"DCCC", "9":"CM", "0":""}
        thous = {"1":"M", "2":"MM", "3":"MMM"}
        number = str(num)
        if len(number) == 1:
            return ones[number[-1]]
        elif len(number) == 2:
            return tens[number[-2]] + ones[number[-1]]
        elif len(number) == 3:
            return hund[number[-3]] + tens[number[-2]] + ones[number[-1]]
        else:
            return thous[number[-4]] + hund[number[-3]] + tens[number[-2]] + ones[number[-1]]


print(Solution().intToRoman(1233))
print(Solution().intToRoman(412))
print(Solution().intToRoman(983))