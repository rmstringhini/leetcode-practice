'''

You're given strings jewels representing the types of stones that are jewels, 
and stones representing the stones you have. Each character in stones is a type 
of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0

'''

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        print("jewels ->", jewels, "stones ->", stones)
        
        aux = []
        aux_stones = list(stones)
        print(aux_stones)
        
        for i in range(len(stones)):
            # print(stones[i])
            # print("____")
            for j in range(len(jewels)):
                # print(jewels[j])
                if stones[i].islower() and jewels[j].islower():
                    if stones[i] == jewels[j]:
                        # print("equal ->", stones[i], jewels[j])
                        aux.append(stones[i])
                    else: print("not equal")
                if stones[i].islower() and jewels[j].isupper():
                    print("not equal")
                if stones[i].isupper() and jewels[j].isupper():
                    if stones[i] == jewels[j]:
                        # print("equal ->", stones[i], jewels[j])
                        aux.append(stones[i])
                    else: print("not equal")
        
        print(aux, len(aux))                
        
        return len(aux)                                          
        
solution = Solution()
jewels = "aAasfdaf"
stones = "aAAbbbb"
solution.numJewelsInStones(jewels, stones)        