#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        left,  right = 0, n - 1
        while left < n - 1 and nums[left] <= nums[left+1]:
            left += 1
        if left == n - 1:  # 连续非递减区间
            return True
        while right > 0 and nums[right-1] <= nums[right]:
            right -= 1
		# 1.一定包含不止一个「峰谷」落差
        if right - left + 1 > 2:
            return False
        # 2.「峰谷」两侧任一不存在元素
        if left == 0 or right == n - 1:  # 两侧无，都对
            return True
        # 3.「峰谷」可修改的区间是否存在？
        if nums[right+1] >= nums[left] or nums[left-1] <= nums[right]:
                return True
        return False


# @lc code=end

