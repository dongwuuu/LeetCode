#
# @lc app=leetcode.cn id=649 lang=python3
#
# [649] Dota2 参议院
#

# @lc code=start
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        
        while senate:
            if senate.count("R") == len(senate):
                return "Radiant"
            if senate.count("D") == len(senate):
                return "Dire"
                
            if senate[0] == "R":
                senate.remove("R")
                senate.remove("D")
                senate.append("R")
            if senate[0] == "D":
                senate.remove("D")
                senate.remove("R")
                senate.append("D")
             
        
# @lc code=end

