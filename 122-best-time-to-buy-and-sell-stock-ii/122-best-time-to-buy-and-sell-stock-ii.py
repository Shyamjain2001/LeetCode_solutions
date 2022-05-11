class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        price=prices[0]
        for i in range(1,len(prices)):
            if price>prices[i]:
                price=prices[i]
            else:
                profit+=prices[i]-price
                price=prices[i]
        return profit
                
                
            
        