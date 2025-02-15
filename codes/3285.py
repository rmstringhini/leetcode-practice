'''
There are n mountains in a row, and each mountain has a height. You are given 
an integer array height where height[i] represents the height of mountain i, 
and an integer threshold.

A mountain is called stable if the mountain just before it (if it exists) has 
a height strictly greater than threshold. Note that mountain 0 is not stable.

Return an array containing the indices of all stable mountains in any order.

 

Example 1:

Input: height = [1,2,3,4,5], threshold = 2

Output: [3,4]

Explanation:

Mountain 3 is stable because height[2] == 3 is greater than threshold == 2.
Mountain 4 is stable because height[3] == 4 is greater than threshold == 2.
'''

class Solution(object):
    def stableMountains(self, height, threshold):
        
        n = len(height)
        ans = []
        for i in range(1,n):
            print("height[",i,"] ->", height[i])
            if height[i-1] > threshold:
                ans.append(i)
        
        return ans
        

solution = Solution()
height = [1,2,3,4,5]
threshold = 2
print(solution.stableMountains(height, threshold))        