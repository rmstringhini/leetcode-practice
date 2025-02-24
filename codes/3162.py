'''
You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. 
You are also given a positive integer k.

A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).

Return the total number of good pairs.

Example 1:

Input: nums1 = [1,3,4], nums2 = [1,3,4], k = 1

Output: 5

Explanation:

The 5 good pairs are (0, 0), (1, 0), (1, 1), (2, 0), and (2, 2).
'''

class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        aux = 0
        count = 0
        
        for i in range(n1):
            for j in range(n2):
                aux = nums2[j] * k
                if nums1[i] % aux == 0:
                    count += 1
                    print(i,j)
        
        return count
        
        
solution = Solution()
nums1 = [1,3,4]
nums2 = [1,3,4]
k = 1
print(solution.numberOfPairs(nums1, nums2, k))        