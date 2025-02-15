import numpy as np

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxCandies = max(candies)
        aux = np.zeros(len(candies))
        booleanArray = []
        # print(len(aux))
        # print(maxCandies)
        for i in range(len(candies)):
            aux[i]  = candies[i] + extraCandies
        
        aux = aux.astype(np.int32)
        # print("aux ->", aux)
        
        for j in range(len(aux)):
            if aux[j] >= maxCandies:
                # print("aux higher than max ->", aux[j])
                booleanArray.append(True)
            else: booleanArray.append(False)
        
        # print("booleanArray ->", booleanArray)
        
        return booleanArray

solution = Solution()
candies = [2,3,5,1,3]
extraCandies = 3
solution.kidsWithCandies(candies, extraCandies)        
            
