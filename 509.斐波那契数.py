#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return Solution().fib(n-1) + Solution().fib(n-2)
# @lc code=end

