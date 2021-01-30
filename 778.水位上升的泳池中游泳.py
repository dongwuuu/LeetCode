#
# @lc app=leetcode.cn id=778 lang=python3
#
# [778] 水位上升的泳池中游泳
#

# @lc code=start
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        heap = [(grid[0][0],0,0)]
        visited = set([(0,0)])
        
        while heap:
            height,x,y = heapq.heappop(heap)
            res = max(res,height)
            if x == n-1 and y == n-1:
                return res
            
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                new_x,new_y = x + dx,y + dy
                if 0 <= new_x < n and 0 <= new_y < n and (new_x,new_y) not in visited:
                    visited.add((new_x,new_y))
                    heapq.heappush(heap,(grid[new_x][new_y],new_x,new_y))
        
        return -1

        
# @lc code=end

