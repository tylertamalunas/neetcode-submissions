class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ 
        keep track of max profit (biggest difference between a value on left and value on right)
        keep track of min to left, if new min is found, use that
        keep track of max, if new min is found, reset max
        """
        maxProfit = 0
        low = prices[0]
        high = 0

        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
                high = 0
            elif prices[i] > high:
                high = prices[i]
            profit = high - low
            maxProfit = max(maxProfit, profit)
        return maxProfit