'''

You are given two strings word1 and word2. Merge the strings by adding letters 
in alternating order, starting with word1. If a string is longer than the other, 
append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

'''

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        word1_aux = list(word1)
        word2_aux = list(word2)
        
        if len(word1_aux) >= len(word2_aux):        
            word2_aux.extend([None] * (len(word1)-len(word2)))
            print("w1 > w2 ->", word2_aux)
        elif len(word2_aux) > len(word1_aux):
            word1_aux.extend([None] * (len(word2)-len(word1)))
            print("w2 > w1 ->", word1_aux)
            
        aux = []
        
        for i in range(len(word1_aux)):  
            aux.append(word1_aux[i])
            aux.append(word2_aux[i])
        
        aux = [item for item in aux if item is not None]                           
        aux = ''.join(aux)
        print(aux)
        
        return aux
            
        
        
solution = Solution()
word1 = "abcd"
word2 = "pq"    
solution.mergeAlternately(word1, word2)    