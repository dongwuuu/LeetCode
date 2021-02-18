#
# @lc app=leetcode.cn id=995 lang=python3
#
# [995] K 连续位的最小翻转次数
#

# @lc code=start
class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        N = len(A)
        res = 0
        for i in range(N - K + 1):
            if A[i] == 1:
                continue
            for j in range(K):
                A[i + j] ^= 1
            res += 1
        for i in range(N):
            if A[i] == 0:
                return -1
        return res


        
# @lc code=end

