#
# @lc app=leetcode.cn id=321 lang=python3
#
# [321] 拼接最大数
#
from typing import List
# @lc code=start
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def get_max_from_nums(nums, k):
            stack = []
            drop = len(nums) - k
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]
        
        def merge(nums1, nums2):
            result = list()
            while nums1 or nums2:
                max_list = nums1 if nums1 > nums2 else nums2
                result.append(max_list[0])
                max_list.pop(0)
            return result

        return max(merge(get_max_from_nums(nums1, i), get_max_from_nums(nums2, k-i)) for i in range(k+1) if i <= len(nums1) and k-i <= len(nums2))

        # ans = []
        # for a in range(k+1):
        #     if a <= len(nums1) and k - a <= len(nums2):
        #         print(ans, merge_nums(get_max_from_nums(nums1, a), get_max_from_nums(nums2, k - a)))
        #         ans = max(ans, merge_nums(get_max_from_nums(nums1, a), get_max_from_nums(nums2, k - a)))
        # return ans
        # @lc code=end
print(Solution().maxNumber([1, 2], [], 2))