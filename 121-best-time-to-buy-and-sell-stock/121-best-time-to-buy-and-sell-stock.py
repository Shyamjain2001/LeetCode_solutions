class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=100000
        sell=-1
        profit=0
        for i in prices:
            if i<buy:
                buy=i
            elif i>buy:
                sell=i
                profit=max(profit,sell-buy)
        return profit