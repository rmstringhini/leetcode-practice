class Solution(object):
    def judgeCircle(self, moves):
                        
        leftRight = 0
        upDown = 0
        
        for m in moves:
            if m == 'U':
                upDown += 1
            elif m =='D':
                upDown -= 1
            elif m == 'L':
                leftRight += 1
            elif m == 'R':
                leftRight -= 1
        
        if leftRight == 0 and upDown == 0:
            return True
        else: return False
                    
                
                
                    
                
                    
            
            
            
            
        
moves = "UDLRLLL"
print(Solution().judgeCircle(moves))        