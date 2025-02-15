'''

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false
 

'''


class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        aux1, aux2 = [], []
        
        aux1.extend(nums)
        aux2.extend(nums)
        
        aux1.sort()
        aux2.sort(reverse=True)
        
        # print(aux1, aux2)
        
        if(aux1 == nums or aux2 == nums):
            return True
        return False    
                
            
        
        
solution = Solution()
nums = [1,2,2,2]
solution.isMonotonic(nums)
        