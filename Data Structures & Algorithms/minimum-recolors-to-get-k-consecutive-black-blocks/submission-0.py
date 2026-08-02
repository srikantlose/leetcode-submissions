class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        blocks=list(blocks)
        for i in range (len(blocks)):
            if blocks[i]=='W':
                blocks[i]=0
            else:
                blocks[i]=1
        print(blocks)
        
        L,R=0,1
        minDiff=float('inf')
        add=blocks[L]
        while R<len(blocks):
            add=add+blocks[R]
            
            if R-L==k-1:
                L+=1
                R=L+1  
                minDiff=min(minDiff,k-add)
                add=blocks[L]
            R+=1
        return minDiff