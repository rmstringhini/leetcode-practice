'''
You are given a string num consisting of only digits. A string of digits is 
called balanced if the sum of the digits at even indices is equal to the sum 
of digits at odd indices.

Return true if num is balanced, otherwise return false.

 

Example 1:

Input: num = "1234"

Output: false

Explanation:

The sum of digits at even indices is 1 + 3 == 4, and the sum of digits at odd
indices is 2 + 4 == 6.
Since 4 is not equal to 6, num is not balanced.
'''

class Solution(object):
    def isBalanced(self, num):
    
        aux = list(num)
        n = len(aux)
        
        even = []
        odd = []
        
        for i in range(n):
            if i % 2 == 0:
                even.append(aux[i])
            else: odd.append(aux[i])
        
        sum_even = 0
        sum_odd = 0
        
        for i in range(len(even)):
            sum_even = sum_even + int(even[i])
        
        for i in range(len(odd)):
            sum_odd = sum_odd + int(odd[i])
        
        if sum_even == sum_odd:
            return True
        else: return False
        
        
        
    
num = "24123"
print(Solution().isBalanced(num))