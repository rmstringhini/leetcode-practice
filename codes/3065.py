'''
You are given a 0-indexed integer array nums, and an integer k.

In one operation, you can remove one occurrence of the smallest element of nums.

Return the minimum number of operations needed so that all elements of the array 
are greater than or equal to k.

 

Example 1:

Input: nums = [2,11,10,1,3], k = 10
Output: 3
Explanation: After one operation, nums becomes equal to [2, 11, 10, 3].
After two operations, nums becomes equal to [11, 10, 3].
After three operations, nums becomes equal to [11, 10].
At this stage, all the elements of nums are greater than or equal to 10 so we can stop.
It can be shown that 3 is the minimum number of operations needed so that all
 elements of the array are greater than or equal to 10.
'''

class Solution(object):
    def minOperations(self, nums, k):

        aux = []
        count = 0
        for n in nums:
            if n < k:
                count += 1
            else: aux.append(n)  
        
        return count
        
nums = [1,1,2,4,9]
k = 9
print(Solution().minOperations(nums, k))        