#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        state, max_length = 0, 1
        for i in range(1, len(nums)):
            if state == 0:
                if nums[i] - nums[i-1] > 0:
                    max_length += 1
                    state = 1
                elif nums[i] - nums[i-1] < 0 :
                    max_length += 1
                    state = -1
                else:
                    continue
            else:
                if (nums[i] - nums[i-1]) * state < 0 :
                    max_length += 1
                    state = nums[i] - nums[i-1]
        return max_length

# @lc code=end

