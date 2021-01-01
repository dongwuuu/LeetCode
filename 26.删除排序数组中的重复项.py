#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        fact_index = 0
        for index in range(0, len(nums)):
            if nums[fact_index] != nums[index]:
                fact_index += 1
                nums[fact_index] = nums[index]
        return fact_index + 1


# @lc code=end

