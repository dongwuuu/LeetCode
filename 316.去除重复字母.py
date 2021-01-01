#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = list()
        from collections import Counter
        char_dict = Counter(s)
        for char in s:
            if char not in stack:
                while stack and char < stack[-1] and char_dict[stack[-1]] > 0:
                    stack.pop()
                stack.append(char)
            char_dict[char] -= 1
        return ''.join(stack)

# @lc code=end
print(Solution().removeDuplicateLetters("bbcaac"))
