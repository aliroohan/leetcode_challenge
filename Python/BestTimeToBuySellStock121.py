class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > max_profit:
                max_profit = prices[i] - buy

        return max_profit


print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([7,6,4,3,1]))