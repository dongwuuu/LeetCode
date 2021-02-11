#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第 K 大元素
#

# @lc code=start

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        self.nums.sort(reverse=True)
    def add(self, val: int) -> int:
        if not self.nums:
            self.nums.append(val)
            return val
        l=len(self.nums)
        for i in range(l):
            if val>self.nums[i]:
                self.nums.insert(i,val)
                break
            if i==l-1:
                self.nums.append(val)
        return self.nums[self.k-1]
            




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

