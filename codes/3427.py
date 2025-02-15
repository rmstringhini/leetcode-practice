'''
You are given an integer array nums of size n. For each index i where 0 <= i < n, define a 
subarray
 nums[start ... i] where start = max(0, i - nums[i]).

Return the total sum of all elements from the subarray defined for each index in the array.

 
Example 1:

Input: nums = [2,3,1]

Output: 11
'''

class Solution(object):
    def subarraySum(self, nums):
        
        n = len(nums)
        ans = 0
        for i in range(n):
            start = max(0, i - nums[i])        
            ans = ans + sum(nums[start:i+1])
            
        
        return ans
            
        
        
nums = [3,1,1,2]
print(Solution().subarraySum(nums))