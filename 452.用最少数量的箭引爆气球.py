#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#
from typing import List
# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        def cover(nums1, nums2):
            if nums1[1] >= nums2[0]:
                return True
        
        if not points:
            return 0

        points.sort()
        print(points)
        stack = [points[0]]
        for item in points:
            print(stack)
            if  cover(stack[-1], item):
                cur_pop = stack.pop()
                stack.append([max(cur_pop[0], item[0]), min(cur_pop[1], item[1])])
            else:
                stack.append(item)
        return len(stack)
        

# @lc code=end
print(Solution().findMinArrowShots([[10,16], [2,8], [1,6], [7,12]]))

