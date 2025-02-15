'''
Given a string s, check if it can be constructed by taking a substring of it 
and appending multiple copies of the substring together.

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
'''

class Solution(object):
    def repeatedSubstringPattern(self, s):
        n = len(s)
        n2 = n// + 1
        for i in range(1, n2):
            if n%i == 0:
                sub = s[:i]
                if sub*(n//i) == s:
                    return True
        return False
                            
s = "abab"
print(Solution().repeatedSubstringPattern(s))        