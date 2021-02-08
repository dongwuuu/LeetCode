#
# @lc app=leetcode.cn id=978 lang=python3
#
# [978] 最长湍流子数组
#

# @lc code=start
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        up = [1] * len(A)
        down = [1] * len(A)
        ans = 1

        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                up[i] = down[i-1] + 1
            elif A[i] < A[i-1]:
                down[i] = up[i-1] + 1
            ans = max(ans, down[i], up[i])
        return ans
            
# @lc code=end

