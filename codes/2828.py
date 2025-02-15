'''
Given an array of strings words and a string s, determine if s is an acronym of words.

The string s is considered an acronym of words if it can be formed by concatenating 
the first character of each string in words in order. For example, "ab" can be 
formed from ["apple", "banana"], but it can't be formed from ["bear", "aardvark"].

Return true if s is an acronym of words, and false otherwise.

 

Example 1:

Input: words = ["alice","bob","charlie"], s = "abc"
Output: true
Explanation: The first character in the words "alice", "bob", 
and "charlie" are 'a', 'b', and 'c', respectively. Hence, s = "abc" is the acronym. 
'''

class Solution(object):
    def isAcronym(self, words, s):
                
        aux_s = list(s)

        if len(words) != len(aux_s):
            return False
        
        count = 0
        
        for i in range(len(words)):
            if words[i][0] == aux_s[i]:
                count += 1
            else:
                return False
        
        if count == len(aux_s):
            return True
        else:
            return False
        

words = ["alice","bob","charlie"]
s = "abc"
print(Solution().isAcronym(words, s))