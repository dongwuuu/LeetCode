#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        curr_row = []
        next_row = [1]
        for i in range(rowIndex):
            # update curr_row
            curr_row = next_row
            # update next_row
            next_row = [0] * (len(curr_row) + 1)
            for j in range(len(next_row)):
                if j == 0 or j == len(next_row) - 1:
                    next_row[j] = 1
                else:
                    next_row[j] = curr_row[j-1] + curr_row[j]
        return next_row

# @lc code=end

