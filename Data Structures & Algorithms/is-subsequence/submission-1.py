class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(len(s)>len(t)):
            return False
        L=[]
        last_used=0
        for i in s:
            idx=t.find(i,last_used)
            #idx=t.index(i)
            L.append(idx)
            last_used=idx
        print (L,sorted(L))
        return True if sorted(L)==L else False