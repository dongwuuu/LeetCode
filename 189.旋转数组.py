#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums = nums[len(nums)-k:] + nums[:len(nums)-k]
        return nums
print(Solution().rotate([1,2,3,4,5,6], 3))
# @lc code=end

