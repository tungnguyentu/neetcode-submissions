class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        index = 1
        for price in prices:
            for next_price in prices[index:]:
                profit = next_price - price
                if profit > max_profit:
                    max_profit = profit
            index += 1
        return max_profit