#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心索引
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
       n = len(nums)
       sumAll = sum(nums)
       sumHalf = 0
       
       for i in range(n):
           if i == 0: sumHalf = 0
           # 满足条件返回 i 的位置，反之继续累加 a 的值，最坏情况循环 n 次
           if sumHalf * 2 + nums[i] == sumAll:
               return i

           sumHalf += nums[i]

       return -1


# @lc code=end

