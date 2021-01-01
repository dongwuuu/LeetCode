#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        dp = [nums[0], max(nums[:2])]
        for i in range(2, len(nums)):
            dp.append(max(nums[i] + dp[-2], dp[-1]))
        return dp[-1]
# @lc code=end

