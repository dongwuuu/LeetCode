#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#

# @lc code=start
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        n = len(A)
        if n < 3: return True
        Increase = False; Decrease = False
        for i in range(1, n):
            if A[i] > A[i - 1]:
                Increase = True
                if Decrease: return False
            elif A[i] < A[i - 1]:
                Decrease = True
                if Increase: return False
        return True

# @lc code=end

