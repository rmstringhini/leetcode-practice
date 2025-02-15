'''

Given two binary strings a and b, return their sum as a binary string.

 
Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        a = int(a, 2)
        b = int(b, 2)
        
        # print(a, b)
        
        add = a + b
        
        add = format(add, 'b')
        # print(add)
       
        return add

    

solution = Solution()
a = '1010'
b = '1011'
solution.addBinary(a, b)
        