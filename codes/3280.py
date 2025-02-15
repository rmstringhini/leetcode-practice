'''
You are given a string date representing a Gregorian calendar date in the yyyy-mm-dd format.

date can be written in its binary representation obtained by converting year, month, 
and day to their binary representations without any leading zeroes and writing them 
down in year-month-day format.

Return the binary representation of date.

 

Example 1:

Input: date = "2080-02-29"

Output: "100000100000-10-11101"

Explanation:

100000100000, 10, and 11101 are the binary representations of 2080, 02, and 29 respectively.

Example 2:

Input: date = "1900-01-01"

Output: "11101101100-1-1"

Explanation:

11101101100, 1, and 1 are the binary representations of 1900, 1, and 1 respectively.
'''

class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        
        if len(date) == 0:
            return 0
        
        date = date.replace('-',' ').split()
        binary = []
        for i in range(len(date)):
            binary.append(format(int(date[i]),'b')+'-')
                        
        binary = ''.join(binary)
        binary = binary[:-1]        

        return binary
        
        
        
solution = Solution()
date = "1900-01-01"
solution.convertDateToBinary(date)