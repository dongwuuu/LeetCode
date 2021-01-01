#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
from itertools import permutations
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # res = [[]]
        total = "()" * n
        res = permutations(total, 6)
        for i in res:
            print("".join(list(i)))

print(Solution().generateParenthesis(3))
        
# @lc code=end

