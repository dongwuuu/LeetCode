#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1 or (len(prices) == 2 and prices[1] <= prices[0]):
            return 0
        dp = [0]
        for i in range(1, len(prices)):
            if prices[i] >= prices[i-1]:
                dp.append(prices[i] - prices[i-1] + dp[-1])
        return dp[-1]
        

        
# @lc code=end

