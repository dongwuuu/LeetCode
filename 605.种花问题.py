#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#
from typing import List
# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if flowerbed[0] == 1 and n == 1:
                return False
            else:
                return True
        for i in range(len(flowerbed)):
            if n == 0:
                break
            if i - 1 >= 0:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    if i+1 < len(flowerbed):
                        if flowerbed[i+1] == 0:
                            n -= 1
                            flowerbed[i] = 1
                    else:
                        flowerbed[i] =1 
                        n -= 1
            else:
                if flowerbed[i+1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    n -= 1
        if n == 0:
            return True
        return False
            


print(Solution().canPlaceFlowers(flowerbed = [0, 0, 1, 0, 1], n = 1))
        
# @lc code=end

