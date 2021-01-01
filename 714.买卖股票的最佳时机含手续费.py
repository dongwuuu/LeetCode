#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        maichu, chiyou = 0, -prices[0]
        for i in range(1, len(prices)):
            maichu = max(maichu, chiyou + prices[i] - fee)
            chiyou = max(chiyou, maichu - prices[i])
        return maichu
        
# @lc code=end

