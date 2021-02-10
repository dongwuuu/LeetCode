#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:                           #长度都不够，肯定匹配不上
            return False
        char_need_num = defaultdict(int)    #某个字母需要的个数  2：还缺2个才匹配  -2：余了2个
        for c in s1:
            char_need_num[c] += 1
        total_need_num = n                  #总共需要的有效个数 迫切需要的（每次出窗入窗要做判断的）

        for i in range(n):
            c = s2[i]
            if c in char_need_num:          #c是s1中的字符  是需要的字符
                if char_need_num[c] > 0:    #还迫切需要
                    total_need_num -= 1
                char_need_num[c] -= 1       #例行统计而已
        if total_need_num == 0:             #整体不缺了
            return True
        
        for r in range(n, m):               #窗口r端遍历
            L, R = s2[r-n], s2[r]           #l端字符  r端字符  维持sliding window 宽度为s1的长度n
            if L in char_need_num:          #是s1中的字符
                if char_need_num[L] >= 0:   #迫切需要 或者刚好维持平衡
                    total_need_num += 1
                char_need_num[L] += 1       #例行统计
            if R in char_need_num:          
                if char_need_num[R] > 0:
                    total_need_num -= 1
                char_need_num[R] -= 1
            if total_need_num == 0:         #整体不缺，刚好匹配
                return True
        
        return False                        #一直在尝试，最终还是没有匹配成功


# @lc code=end

