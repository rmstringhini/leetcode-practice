'''
You are given an integer n and an integer start.

Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.

 

Example 1:

Input: n = 5, start = 0
Output: 8
Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.
'''

class Solution(object):
    def xorOperation(self, n, start):

        nums = [0] * n
        
        for i in range(n):
            nums[i] = start + 2 * i
        
        ans = 0
        
        for j in nums:
            ans ^= j
        
        return ans
     
        
        
                
        
        
n = 4
start = 3
print(Solution().xorOperation(n, start))        