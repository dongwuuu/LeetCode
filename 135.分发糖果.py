#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#
from typing import List
# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        left2right = [1] * len(ratings)
        right2left = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                left2right[i] = left2right[i-1] + 1
        
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right2left[i] = right2left[i+1] + 1
        return sum([max(left2right[i], right2left[i]) for i in range(len(ratings))])

# @lc code=end
print(Solution().candy([1, 0, 2]))
