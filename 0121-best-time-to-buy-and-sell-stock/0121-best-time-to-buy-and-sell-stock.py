class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_buy = prices[0]
        best_buy = prices[0]
        best_sell = prices[0]
        for i in range(1, len(prices)):
            if prices[i] - best_buy > best_sell - cur_buy:
                best_sell = prices[i]
                cur_buy = best_buy
            elif prices[i] < best_buy:
                best_buy = prices[i]
        return(best_sell - cur_buy)