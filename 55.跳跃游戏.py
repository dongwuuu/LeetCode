#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        
        index, jump= [], 0
        for i in range(len(nums)):
            index.append(nums[i] + i)
        max_index = index[0]
        while jump < len(index) and jump <= max_index:
            if index[jump] >= max_index:
                max_index = index[jump]
            jump += 1
        if max_index + 1 >= len(index):
            return True
        else:
            return False
# @lc code=end

