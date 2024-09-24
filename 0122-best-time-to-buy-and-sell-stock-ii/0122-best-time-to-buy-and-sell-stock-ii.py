class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        st_in = 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                profit += prices[i-1] - prices[st_in]
                st_in = i
        if prices[st_in] < prices[-1]:
            profit += prices[-1] - prices[st_in]
        return profit