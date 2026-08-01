class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]

        for i in asteroids:
            if(i<0 and stack and stack[-1]>0):
                while(stack and abs(i)>stack[-1]):
                    stack.pop()
                if stack[-1]==abs(i):
                    stack.pop()
                elif(abs(i)<stack[-1]):
                    continue
                else:
                    stack.append(i)
            elif(i>0 or not stack):
                stack.append(i)
        return stack