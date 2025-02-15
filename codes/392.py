'''

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by 
deleting some (can be none) of the characters without disturbing the relative positions 
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

'''


from collections import Counter

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        check = s
        test = t
        
        if not check:
            return True
        
        if not test:
            return False
        
        pointer = 0
        
        for char in test:
            if pointer < len(check) and char == check[pointer]:
                pointer += 1
            if pointer == len(check):                
                return True
        
        return False
        
        

solution = Solution()

s = "acb"
t = "ahbgdc"

solution.isSubsequence(s, t)