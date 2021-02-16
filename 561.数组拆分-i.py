#
# @lc app=leetcode.cn id=561 lang=python3
#
# [561] 数组拆分 I
#

# @lc code=start
class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        res = 0
        for i in range(0, len(nums), 2):
            res += min(nums[i], nums[i + 1])
        return res


# @lc code=end

