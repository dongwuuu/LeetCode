#
# @lc app=leetcode.cn id=989 lang=python3
#
# [989] 数组形式的整数加法
#

# @lc code=start
        
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        K = list(map(int,str(K)))
        
        res = []
        i,j = len(A)-1,len(K)-1
        carry = 0

        while i >= 0 and j >= 0:
            res.append(A[i] + K[j] + carry)
            res[-1],carry = res[-1] % 10, res[-1] // 10
            i -= 1
            j -= 1
        while i >= 0:
            res.append(A[i] + carry)
            res[-1],carry = res[-1] % 10, res[-1] // 10
            i -= 1
        while j >= 0:
            res.append(K[j] + carry)
            res[-1],carry = res[-1] % 10, res[-1] // 10
            j -= 1

        if carry:
            res.append(1)

        return res[::-1]

# @lc code=end

