'''
You are given positive integers n and m.

Define two integers as follows:

num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.
Return the integer num1 - num2.

 

Example 1:

Input: n = 10, m = 3
Output: 19
Explanation: In the given example:
- Integers in the range [1, 10] that are not divisible by 3 are [1,2,4,5,7,8,10], 
num1 is the sum of those integers = 37.
- Integers in the range [1, 10] that are divisible by 3 are [3,6,9], num2 is 
the sum of those integers = 18.
We return 37 - 18 = 19 as the answer.
'''

class Solution(object):
    def differenceOfSums(self, n, m):

        div = []
        not_div = []
        
        for i in range(1,n+1):
            if i % m != 0:
                not_div.append(i)
            else: div.append(i)
            
        print(div, not_div)

        sum_div = sum(div)
        sum_not = sum(not_div)
        
        return (sum_not - sum_div)
        

solution = Solution()
n = 10
m = 3
print(solution.differenceOfSums(n,m))
        