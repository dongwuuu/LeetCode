#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == len(t):
            return s == t

        s_stack, t_stack = list(s), list(t)
        while s_stack and t_stack:
            if s_stack[0] == t_stack[0]:
                s_stack.pop(0)
                t_stack.pop(0)
            else:
                t_stack.pop(0)

        return not s_stack
# @lc code=end
print(Solution().isSubsequence('axc', "ahbgdc"))

