'''

Given an integer num, repeatedly add all its digits until the result has only
one digit, and return it.

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0

'''

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        print(num)
        str_num = str(num)
        print("str num ->", str_num, str_num.split())
        
solution = Solution()
num = 38
solution.addDigits(num)        