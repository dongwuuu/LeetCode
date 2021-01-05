#
# @lc app=leetcode.cn id=830 lang=python3
#
# [830] 较大分组的位置
#
from typing import List
# @lc code=start
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        left, right = 0, 0

        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(i)
            elif s[stack[-1]] == s[i]:
                stack.append(i)
            elif s[stack[-1]] != s[i]:
                if stack[-1] - stack[0] >= 2:
                    res.append([stack[0], stack[-1]])
                stack = [i]
            print(stack)
        if stack[-1] - stack[0] >= 2:
            res.append([stack[0], stack[-1]])
        return res

print(Solution().largeGroupPositions("aaa"))
# @lc code=end

