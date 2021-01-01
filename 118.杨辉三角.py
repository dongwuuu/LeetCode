#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
from typing import List
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []

        res = [[1], [1, 1]]
        if 0 < numRows <= 2:
            return res[:numRows]
        for i in range(3, numRows+1):
            temp = [1] * i
            for j in range(1, i-1):
                temp[j] = res[-1][j] + res[-1][j-1]
            res.append(temp)
        return res
print(Solution().generate(2))
# @lc code=end

