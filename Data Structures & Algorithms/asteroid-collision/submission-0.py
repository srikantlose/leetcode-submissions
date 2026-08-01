class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        
        for i in asteroids:
            if not stack:
                if i>0:
                    stack.append(i)
                    continue
                else:
                    continue
                
            


            elif abs(stack[-1])==abs(i) and i<0:
                stack.pop()
                continue

            if abs(stack[-1])<abs(i) and i<0:
                while(abs(stack[-1]) < abs(i)):
                    stack.pop()


            elif(i<0):
                continue
            else:
                
                stack.append(i)
                
                
        return stack

        