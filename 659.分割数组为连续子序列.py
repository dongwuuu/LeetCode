#
# @lc app=leetcode.cn id=659 lang=python3
#
# [659] 分割数组为连续子序列
#

# @lc code=start
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return False
        res = list()
        for n in nums:
            for v in res:
                if v[-1] + 1 == n:
                    v.append(n)
                    break
            else:
                res.insert(0, [n])
        return all(len(x) > 2 for x in res)

# @lc code=end

