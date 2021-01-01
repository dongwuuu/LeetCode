#
# @lc app=leetcode.cn id=502 lang=python3
#
# [502] IPO
#
from heapq import nlargest
from typing import List
# @lc code=start
class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        if W >= max(Capital):
            return W + sum(nlargest(k, Profits))
        
        for index in range(min(k, len(Profits))):
            target_index = -1
            for i in range(len(Profits)):
                if W >= Capital[i]:
                    if target_index == -1:
                        target_index = i
                    elif Profits[i] > Profits[target_index]:
                        target_index = i
            if target_index == -1:
                break
            W += Profits[target_index]
            Capital[target_index] = float('inf')


        return W


# @lc code=end
print(Solution().findMaximizedCapital(2, 0, [1,2,3], [0,1,1]))