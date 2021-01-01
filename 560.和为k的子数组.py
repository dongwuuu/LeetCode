#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = []
        point = 0
        temp = 0
        for i in range(len(nums)):
            if i == 0:
                while temp < k:
                    temp += nums[point]
                    point += 1
            else:
                
            if temp == k:
                res.append(nums[i:point+1])
                temp = 0

# @lc code=end

