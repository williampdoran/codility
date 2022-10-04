from typing import List
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(0, len(prices)):
            for j in range(i, len(prices)):
                diff = prices[j] - prices[i]
                profit = max(profit, diff)
        return profit

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        # Not enough time to earn profit
        if len(prices) < 2:        return 0
        # The maximum price from here to the end
        maxFromHere = prices[-1]
        # The maximum profit, we could earn.
        # Could initialize it with any valid profit.
        maxProfit = prices[1] - prices[0]
        for index in range(len(prices)-2, -1, -1):
            price = prices[index]
            # The maximum profit, if we buy it here.
            profit = maxFromHere - price
            maxProfit = max(maxProfit, profit)
            maxFromHere = max(maxFromHere, price)
        # If maxProfit is negative, we would not take
        # any transaction.
        #
        # If we initialize the maxProfit with 0, this
        # step is not necessary.
        maxProfit = max(0, maxProfit)
        return maxProfit

    def maxProfitDynamicProgramming(self, prices):
        n = len(prices)
        if len(prices) < 2:
            return 0
        else:
            m = prices[0]
            dp = [0] * n
            for i in range(n):
                print(dp, m)
                dp[i] = prices[i] - m
                if m > prices[i]:
                    m = prices[i]
        return max(dp)

    def solution(self, A):
        if len(A) < 2: return 0
        max_to_here, max_profit = A[-1], 0
        for i in range(len(A) - 2, -1, -1):
            max_to_here = max(max_to_here, A[i])
            max_profit = max(max_to_here - A[i], max_profit)
            print(max_profit, max_to_here)
        return max_profit


# print(Solution().maxProfit([7,1,5,3,6,4]))
# print(Solution().maxProfit([7,6,4,3,1]))

print(Solution().maxProfitDynamicProgramming([23171,21011,21123,21366,21013,21367]))
print(Solution().solution([23171,21011,21123,21366,21013,21367]))
