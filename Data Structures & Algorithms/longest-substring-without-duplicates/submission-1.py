class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L,R,diff,maxDiff=0,0,0,float('-inf')
        
        seen=[]
        while R<len(s):
            if s[R] not in seen:
                seen.append(s[R])
                diff=R-L
                maxDiff=max(maxDiff,diff)
                print(maxDiff)
            else:
                L= L+1 if(seen[len(seen)-1]!=s[R]) else R
            R+=1
            
        return maxDiff+1 if maxDiff!='-inf' else  0


        