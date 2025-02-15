'''

A sequence of numbers is called an arithmetic progression if the difference 
between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to 
form an arithmetic progression. Otherwise, return false.

 

Example 1:

Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 
and -2 respectively, between each consecutive elements.
Example 2:

Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.

'''

class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        
        n = len(arr)
        
        arr = sorted(arr)
        
        if n <= 2: return True
        
        diff = arr[1] - arr[0]
        
        for i in range(1,n-1):
            if arr[i+1] - arr[i] != diff:
                return False
        return True
        
arr = [-13,-17,-8,-10,-20,2,3,-19,2,-18,-5,7,-12,18,-17,12,-1]       
print(Solution().canMakeArithmeticProgression(arr))        