'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum 
average value and return this value. Any answer with a calculation error less 
than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
'''

class Solution(object):
    def findMaxAverage(self, nums, k):

        print(nums, k)
        
        aux = sorted(nums)
        
        aux_ = [0] * k
        
        for i in range(len(aux_)):
            print("- - - i - - -", i)
            for j in range(len(aux)):
                print("aux j ->", abs(aux[j]))
                if abs(aux[j]) >= k:
                    aux_[i] = aux[j]
        
        print(aux_)
                
                

nums = [1, 12, -5, -6, 50, 3]
k = 4
print(Solution().findMaxAverage(nums, k))        