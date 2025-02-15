'''

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        print(nums1, "///", nums2)
        
        merged_list = nums1 + nums2
        merged_list.sort()
        print(merged_list, len(merged_list)%2)
        
        idx = int((len(merged_list)-1)/2)
        
        if len(merged_list) % 2 == 0: # even
            median = (float(merged_list[idx] + merged_list[idx+1])/2)            
            print("median ->", median)
        else: # odd
            median = float(merged_list[idx])
            print("median ->", median)
            
        
        return median
        

solution = Solution()
nums1 = [6,1]
nums2 = [8,3]        
solution.findMedianSortedArrays(nums1, nums2)