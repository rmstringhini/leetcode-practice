class Solution(object):
    def calPoints(self, operations):
        
        print(operations)
        
        stack = []
        
        for op in operations:
            if op.lstrip('-').isnumeric():
                op = int(op)
                print("op ->", op)
                stack.append(op)
                print(stack)
                
            if op == 'C':
                if stack:
                    stack.pop()
                print(stack)
                
            if op == 'D':
                if stack:
                    top = stack[-1]
                    top = int(top) * 2
                    stack.append(top)
                print(stack)
                
            if op == '+':
                if len(stack) >= 2:
                    top = stack[-1] + stack[-2]
                    stack.append(top)
                print(stack)
        
        return sum(stack)
            
        
                
                
                
            
            

operations = ["5","-2","4","C","D","9","+","+"]
print(Solution().calPoints(operations))                