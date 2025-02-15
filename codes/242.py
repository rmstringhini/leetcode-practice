'''
Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        s_list = list(s)
        t_list = list(t)        
        
        s_list = sorted(s_list)
        t_list = sorted(t_list)
        print(s_list, t_list)
        
        if len(s_list) != len(t_list):
            print("not an anagram")
            return False
        elif s_list != t_list:
            print("not an anagram")
            return False
        else: 
            print("anagram")
            return True
            
           
        
        
solution = Solution()
s = 'anagram'
t = 'ganamra'
solution.isAnagram(s, t)        