#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s or not g:
            return 0
        g.sort()
        s.sort()
        g_index, s_index = 0, 0
        while g_index < len(g) and s_index < len(s):
            if s[s_index] >= g[g_index]:
                s_index += 1
                g_index += 1
            else:
                s_index += 1
        return g_index


# @lc code=end

