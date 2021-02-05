#
# @lc app=leetcode.cn id=1208 lang=python3
#
# [1208] 尽可能使字符串相等
#

# @lc code=start
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        accDiff = [0] + list(accumulate(abs(ord(sc) - ord(tc)) for sc, tc in zip(s, t)))
        maxLength = 0

        for i in range(1, n + 1):
            start = bisect.bisect_left(accDiff, accDiff[i] - maxCost)
            maxLength = max(maxLength, i - start)
        
        return maxLength


# @lc code=end

