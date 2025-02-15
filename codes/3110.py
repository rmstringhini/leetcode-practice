'''
You are given a string s. The score of a string is defined as the sum of the absolute 
difference between the ASCII values of adjacent characters.

Return the score of s.

 

Example 1:

Input: s = "hello"

Output: 13

Explanation:

The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. 
So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

Example 2:

Input: s = "zaz"

Output: 50

Explanation:

The ASCII values of the characters in s are: 'z' = 122, 'a' = 97. So, the score of s 
would be |122 - 97| + |97 - 122| = 25 + 25 = 50.
'''

class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        print(s)
        s_list = list(s)
        print(s_list)
        
        ascii_val = [ord(c) for c in s_list]
        print("ascii vals ->", ascii_val)
        
        aux = []
        
        n = len(s_list)
        
        for i in range(n-1):
            print("i ->", ascii_val[i])
            # for j in range(1, n):
            print(ascii_val[i]-ascii_val[i+1])
            aux.append(abs(ascii_val[i]-ascii_val[i+1]))

        print(aux)
        
        res = sum(aux)
        print(res)
        
        return res
        
solution = Solution()
s = "zaz"
solution.scoreOfString(s)