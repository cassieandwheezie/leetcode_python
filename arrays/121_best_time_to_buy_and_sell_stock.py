'''
This is a conceptual code. Assuming if we buy the stock on lowest price and sell at highest price will lead to wrong results.
Buying at a low price and selling at higher price leads to profit in the case when we buy at low price and do not sell it .
My earlier code failed here 
-->[2,4,1]
buying at price 1 and not selling leads to loss but buying at 2 and selling at 4 leads to profit 
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                profit = max(profit, prices[i] - min_price)

        return profit
