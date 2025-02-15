import numpy as np

'''

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

'''


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        print(s)
        
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        aux_list = list(s)
        print(aux_list)
        
        
    
    
solution = Solution()
s = 'IceCream'
solution.reverseVowels(s)         