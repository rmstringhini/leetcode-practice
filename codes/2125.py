'''
Anti-theft security devices are activated inside a bank. You are given a 
0-indexed binary string array bank representing the floor plan of the bank,
which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's 
and '1's. '0' means the cell is empty, while'1' means the cell has a security device.

There is one laser beam between any two security devices if both conditions are met:

The two devices are located on two different rows: r1 and r2, where r1 < r2.
For each row i where r1 < i < r2, there are no security devices in the ith row.
Laser beams are independent, i.e., one beam does not interfere nor join with another.

Return the total number of laser beams in the bank.

Input: bank = ["011001","000000","010100","001000"]
Output: 8
Explanation: Between each of the following device pairs, there is one beam. In total, there are 8 beams:
 * bank[0][1] -- bank[2][1]
 * bank[0][1] -- bank[2][3]
 * bank[0][2] -- bank[2][1]
 * bank[0][2] -- bank[2][3]
 * bank[0][5] -- bank[2][1]
 * bank[0][5] -- bank[2][3]
 * bank[2][1] -- bank[3][2]
 * bank[2][3] -- bank[3][2]
Note that there is no beam between any device on the 0th row with any on the 3rd row.
This is because the 2nd row contains security devices, which breaks the second condition.

'''

class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
            
        n = len(bank)
        m = len(bank[0])
        ans = []
        
        for i in range(n):
            if bank[i].count('1') != 0:
                ans.append(bank[i].count('1'))
        
        n_ans = len(ans)
        out = 0
        for i in range(n_ans-1):
            out += ans[i] * ans[i+1]
        
        return out
            
                
                
        
            
                    
        
solution = Solution()
bank = ["011001","000000","010100","001000"]
print(solution.numberOfBeams(bank))        