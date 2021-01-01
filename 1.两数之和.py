#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1:
            return []
        for left in range(len(nums)):
            for right in range(left+1, len(nums)):
                if nums[left] + nums[right] == target:
                    return [left, right]
        # if len(nums) <= 1:
        #     return []
        # item_index_dict = dict()
        # for index, item in enumerate(nums):
        #     if item not in item_index_dict:
        #         item_index_dict[item] = [index]
        #     item_index_dict[item].append(index)
        # if target % 2 == 0 and len(item_index_dict[target / 2]) >= 2:
        #     return item_index_dict[target / 2][:2] 
        # for key, item in item_index_dict.items():
        #     if target - key in item_index_dict and item_index_dict[target - key] != item:
        #         return [item, item_index_dict[target - key]]
# @lc code=end

