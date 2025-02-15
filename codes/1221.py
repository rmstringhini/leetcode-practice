'''
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it into some number of substrings such that:

Each substring is balanced.
Return the maximum number of balanced strings you can obtain.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring 
contains same number of 'L' and 'R'.
'''

class Solution(object):
    def balancedStringSplit(self, s):

        n = len(s)
        
        aux = 0
        ans = 0
        for i in range(n):
            if s[i] == 'L':
                aux += 1
            else: aux -= 1
            if aux == 0:
                ans +=1
                
        return ans
                

        
s = "LLLLRRRR"
print(Solution().balancedStringSplit(s))        