'''
You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

 

Example 1:

Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
'''


class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        s = list(s)
        print("string ->", s)
        print("indices ->", indices)
        
        target = [''] * len(s)
        
        for i in range(len(s)):
            target[indices[i]] = s[i]
        target = ''.join(target)
        print("output ->", target)        
        return target
        
        
        
solution = Solution()
s = "codeleet" 
indices = [4,5,6,7,0,2,1,3]
solution.restoreString(s, indices)