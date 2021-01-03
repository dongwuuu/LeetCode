#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == "*":
            return True
        s_index, p_index = 0, 0
        
# @lc code=end

