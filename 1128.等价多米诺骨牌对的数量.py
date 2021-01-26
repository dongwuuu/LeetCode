#
# @lc app=leetcode.cn id=1128 lang=python3
#
# [1128] 等价多米诺骨牌对的数量
#

# @lc code=start
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        if len(dominoes) == 0 or len(dominoes[0]) == 0:
            return 0
        
        pairNum = 0
        
        for i in range(len(dominoes)-1):
            for j in range(i+1, len(dominoes)):
                if dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1]:
                    pairNum += 1
                elif dominoes[i][0] == dominoes[j][1] and dominoes[i][1] == dominoes[j][0]:
                    pairNum += 1
        return pairNum

        
# @lc code=end

