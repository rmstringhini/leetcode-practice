'''

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter 
in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".

'''

class Solution(object):
    def wordPattern(self, pattern, s):
        pattern = list(pattern)
        s = s.split()
        
        
                    
        
        
        

pattern = "aaaa"
s = "dog cat cat dog"       

print(Solution().wordPattern(pattern, s))        