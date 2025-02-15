'''

You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. 
Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500
Example 2:

Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000

'''

class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        
        if len(salary) == 0:
            return 0
        
        if len(salary) == 1:
            res = salary[0]
            print(res)
            return res
        
        if len(salary) == 2:
            res = (salary[0] + salary[1]) / len(salary)
            print(res)
            return res
        
        
        ordered = sorted(salary)
        # print(ordered)
        
        cut = ordered[1:-1]
        cut = [float(x) for x in cut]
        print(cut)
        # print(sum(cut)/len(cut))
        
        res = 0.0
        
        res = sum(cut)/len(cut)
        print(res)
        
        return res
        
        
        
solution = Solution()
salary = [48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,
          4000,54000,67000,6000,1000,11000]
solution.average(salary)        