#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        left, right = 0, 0
        while right + 1 < len(nums):
            if nums[right] + 1 == nums[right + 1]:
                right += 1
            else:
                if left != right:
                    res.append(str(nums[left]) + "->" + str(nums[right]))
                else:
                    res.append(str(nums[left]))
                left = right + 1
                right += 1
        if left != right:
            res.append(str(nums[left]) + "->" + str(nums[right]))
        else:
            res.append(str(nums[left]))
        # res.append("\"" + str(nums[left]) + "->" + str(nums[right]) + "\"")
        return res


print(Solution().summaryRanges([0,1,2,4,5,7]))
# @lc code=end

