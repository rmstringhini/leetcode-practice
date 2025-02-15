'''
You are given a 0-indexed integer array nums and an integer k.

Return an integer that denotes the sum of elements in nums whose corresponding
indices have exactly k set bits in their binary representation.

The set bits in an integer are the 1's present when it is written in binary.

For example, the binary representation of 21 is 10101, which has 3 set bits.
 

Example 1:

Input: nums = [5,10,1,5,2], k = 1
Output: 13
Explanation: The binary representation of the indices are: 
0 = 0002
1 = 0012
2 = 0102
3 = 0112
4 = 1002 
Indices 1, 2, and 4 have k = 1 set bits in their binary representation.
Hence, the answer is nums[1] + nums[2] + nums[4] = 13.
'''

class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        
        n = len(nums)
        res = 0
        for i in range(n):
            bin_num = format(i, 'b')
            if bin_num.count('1') == k:
                res = res + nums[i]
        
        return res
                
        
nums = [4,3,2,1]
k = 2
print(Solution().sumIndicesWithKSetBits(nums, k))        