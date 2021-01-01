#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] 移掉K位数字
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numStack = []
        #k的条件下过一遍数组 维持单调递增栈
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1
        
            numStack.append(digit)
        #剩下的k次用完
        finalStack = numStack[:-k] if k else numStack

        return "".join(finalStack).lstrip('0') or "0"

        
# @lc code=end

