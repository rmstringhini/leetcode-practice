'''
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).


Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].

'''

class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        # Calculate the count of odd numbers
        res = (high - low) // 2 + (low % 2 or high % 2)
        
        print(res)
        
        return res

        
        
solution = Solution()
low = 3
high = 7
solution.countOdds(low, high)        