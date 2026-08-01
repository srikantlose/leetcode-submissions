class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L,R,count,countMax=0,0,0,0
        prev=s[0]
        ogK=k
        while R<len(s):
            if(s[R]!=prev and k!=0):
                k-=1
                count+=1
                R+=1
                continue
            elif(s[R]!=prev and k==0):
                L=R
                k=ogK
                count=0
                
            else:
                count+=1
            countMax=max(countMax,count)
            prev=s[R]
            R+=1
        return countMax


                
            