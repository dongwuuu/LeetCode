#
# @lc app=leetcode.cn id=1438 lang=python3
#
# [1438] 绝对差不超过限制的最长连续子数组
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        s = SortedList()
        n = len(nums)
        left = right = ret = 0

        while right < n:
            s.add(nums[right])
            while s[-1] - s[0] > limit:
                s.remove(nums[left])
                left += 1
            ret = max(ret, right - left + 1)
            right += 1
        
        return ret

# @lc code=end

