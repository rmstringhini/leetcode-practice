'''
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.

 

Example 1:

Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
Output: 6
Explanation: 
- The first sentence, "alice and bob love leetcode", has 5 words in total.
- The second sentence, "i think so too", has 4 words in total.
- The third sentence, "this is great thanks very much", has 6 words in total.
Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.
'''

class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        
        n = len(sentences)
        print(sentences[1].split())
        
        
        aux = []
        for i in range(n):
            s = len(sentences[i].split())
            aux.append(s)
        
        return max(aux)
        
        

solution = Solution()
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(solution.mostWordsFound(sentences))        