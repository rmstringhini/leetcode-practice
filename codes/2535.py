'''
You are given a positive integer array nums.

The element sum is the sum of all the elements in nums.
The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
Return the absolute difference between the element sum and digit sum of nums.

Note that the absolute difference between two integers x and y is defined as |x - y|.

 

Example 1:

Input: nums = [1,15,6,3]
Output: 9
Explanation: 
The element sum of nums is 1 + 15 + 6 + 3 = 25.
The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
The absolute difference between the element sum and digit sum is |25 - 16| = 9.
'''

class Solution(object):
    def differenceOfSum(self, nums):

        aux_1 = 0
        aux_2 = 0
        
        digits = [[int(digit) for digit in str(num)] for num in nums]
        
        for i in nums:
            aux_1 = aux_1 + i
        
        for j in range(len(digits)):
            aux_2 = aux_2 + (sum(digits[j]))
        
        return abs(aux_1 - aux_2)
        

        
        
        
nums = [1,15,6,3]   
print(Solution().differenceOfSum(nums))        