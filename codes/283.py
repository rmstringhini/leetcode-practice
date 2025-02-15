'''

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

'''

import numpy as np

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        move_number = 0
        
        nums.sort(key=lambda i: i == move_number)
        
        print("moved 0s ->", nums)
        
        
solution = Solution()
nums = [0]
solution.moveZeroes(nums)