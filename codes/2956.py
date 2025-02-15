'''
You are given two integer arrays nums1 and nums2 of sizes n and m, respectively. 
Calculate the following values:

answer1 : the number of indices i such that nums1[i] exists in nums2.
answer2 : the number of indices i such that nums2[i] exists in nums1.
Return [answer1,answer2].

 

Example 1:

Input: nums1 = [2,3,2], nums2 = [1,2]

Output: [2,1]
'''

class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        aux = []
        count1 = 0
        count2 = 0
        
        for i in nums1:
            if i in nums2:
                count1 += 1
        
        for i in nums2:
            if i in nums1:
                count2 += 1
        
        return [count1, count2]

solution = Solution()
nums1 = [4,3,2,3,1]
nums2 = [2,2,5,2,3,6]
print(solution.findIntersectionValues(nums1, nums2))