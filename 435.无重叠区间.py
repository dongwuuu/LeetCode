#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#
from typing import List
# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 0:
            return 0
        intervals.sort(key=lambda x:(x[0], x[1]))
        
        result, left, right = 0, intervals[0][0], intervals[0][1]

        for index in range(1, len(intervals)):
            cur_left = intervals[index][0]
            cur_right = intervals[index][-1]

            if cur_left < right:
                if cur_right <= right:
                    result += 1
                    right = cur_right
                    left = cur_left
                elif cur_right > right:
                    result += 1
            else:
                right = cur_right
             
        return result
# @lc code=end

print(Solution().eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))