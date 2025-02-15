'''
Given an integer array nums and an integer k, return the number of pairs (i, j) 
where i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0.
 

Example 1:

Input: nums = [1,2,2,1], k = 1
Output: 4
Explanation: The pairs with an absolute difference of 1 are:
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
'''

class Solution(object):
    def countKDifference(self, nums, k):
        
        n = len(nums)
        count = 0
        for i in range(n-1):
            for j in range(i,n):
                if abs(nums[i] - nums[j]) == k:
                    count += 1
        return count

nums = [1,2,2,1]
k = 1
print(Solution().countKDifference(nums, k))
        