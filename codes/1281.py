'''
Given an integer number n, return the difference between the product of its 
digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21

'''

class Solution(object):
    def subtractProductAndSum(self, n):

        aux = str(n)
        
        n = len(aux)
        
        prod = []
        add = []
        
        
        for i in range(n):
            add.append(int(aux[i]))
            prod.append(int(aux[i])) 
    
        add = sum(add)
        
        p = 1
        for i in range(len(prod)):
            p *= prod[i]
        
        return (p - add)
        
        
        
n = 4421
print(Solution().subtractProductAndSum(n))        