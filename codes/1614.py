'''
Given a valid parentheses string s, return the nesting depth of s. 
The nesting depth is the maximum number of nested parentheses.

 

Example 1:

Input: s = "(1+(2*3)+((8)/4))+1"

Output: 3

Explanation:

Digit 8 is inside of 3 nested parentheses in the string.
'''

class Solution(object):
    def maxDepth(self, s):
        
        count = 0
        nestingDepth = 0
        for char in s:
            if char == '(':
                count += 1
            if char == ')':
                count -= 1
            if count > nestingDepth:
                nestingDepth = count
        
        return nestingDepth
        
        
solution = Solution()
s = "(1+(2*3)+((8)/4))+1"
print(solution.maxDepth(s))        