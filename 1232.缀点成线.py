#
# @lc app=leetcode.cn id=1232 lang=python3
#
# [1232] 缀点成线
#

# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        return all((coordinates[1][0] - coordinates[0][0])*(y - coordinates[0][1]) == (coordinates[1][1] - coordinates[0][1])* (x - coordinates[0][0])  
        for x,y in coordinates[2:])


# @lc code=end

