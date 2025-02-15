'''
Given an array of strings words, return the first palindromic string in the array. 
If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.

 

Example 1:

Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.
'''

class Solution(object):
    def firstPalindrome(self, words):

        for w in words:
            reverse_w = w[::-1]
            if w == reverse_w:
                return w
        return ""

words = ["abc","car","ada","racecar","cool"]        
print(Solution().firstPalindrome(words))