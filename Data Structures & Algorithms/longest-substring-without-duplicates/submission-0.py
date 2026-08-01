class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L,R,diff,maxDiff=0,0,0,float('-inf')
        seen=[]
        while R<len(str):
            if str[R] not in seen:
                seen.append(str[R])
                diff=R-L
                maxDiff=max(maxDiff,diff)
            else:
                seen=[]
                L+=1
            R+=1
            return maxDiff if maxDiff!='-inf' else  0


        