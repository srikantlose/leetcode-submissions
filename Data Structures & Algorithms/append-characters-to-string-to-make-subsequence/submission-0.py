class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        stack=[]
        idx=0
        for i in range(len(t)-1,-1,-1):
            stack.append(t[i])
        #print(stack)
        for i in range(len(t)):
            if stack and s[i]==stack[-1]:
                stack.pop()
                if not stack: return 0
                continue
            else:
                
                idx=i
                break
        return len(t)-idx

