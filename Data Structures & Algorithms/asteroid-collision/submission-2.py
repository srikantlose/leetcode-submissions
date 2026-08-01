class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]

        for i in asteroids:
            if not stack:
                stack.append(i)
                continue
            if stack[-1]>0 and i<0:
                if(abs(i)>stack[-1] ):
                    while(stack[-1]<abs(i)):
                        if(len(stack)>1):
                            stack.pop()
                        else:
                            stack.pop()
                            break
                elif(abs(i)==stack[-1]):
                    stack.pop()
                    continue
                else:
                    continue
            elif(stack[-1]<0 and i<0):
                stack.append(i)
            elif i>0:
                stack.append(i)
        return stack