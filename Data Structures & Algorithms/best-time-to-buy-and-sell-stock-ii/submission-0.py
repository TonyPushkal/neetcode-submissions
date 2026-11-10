class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        holding = False
        for i in range(len(prices)-1):
            if not holding and prices[i] < prices[i+1]:
                output -= prices[i]
                holding = True
            if holding and prices[i] > prices[i+1]:
                output += prices[i]
                holding = False

        if holding:
            output += prices[-1]
        return output
        