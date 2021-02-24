#
# @lc app=leetcode.cn id=1052 lang=python3
#
# [1052] 爱生气的书店老板
#

# @lc code=start
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        N = len(customers)
        sum_ = 0
        # 所有不生气时间内的顾客总数
        for i in range(N):
            if grumpy[i] == 0:
                sum_ += customers[i]
        # 生气的 X 分钟内，会让多少顾客不满意
        curValue = 0
        # 先计算起始的 [0, X) 区间
        for i in range(X):
            if grumpy[i] == 1:
                curValue += customers[i]
        resValue = curValue
        # 然后利用滑动窗口，每次向右移动一步
        for i in range(X, N):
            # 如果新进入窗口的元素是生气的，累加不满意的顾客到滑动窗口中
            if grumpy[i] == 1:
                curValue += customers[i]
            # 如果离开窗口的元素是生气的，则从滑动窗口中减去该不满意的顾客数
            if grumpy[i - X] == 1:
                curValue -= customers[i - X]
            # 求所有窗口内不满意顾客的最大值
            resValue = max(resValue, curValue)
        # 最终结果是：不生气时的顾客总数 + 窗口X内挽留的因为生气被赶走的顾客数
        return sum_ + resValue


        
# @lc code=end

