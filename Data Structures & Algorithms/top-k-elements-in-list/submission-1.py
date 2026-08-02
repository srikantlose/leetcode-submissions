class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        for i in nums:
            if i not in hm:
                hm[i]=1
            else:
                hm[i]+=1
        freq=[]
        for i,j in hm.items():
            freq.append((i,j))
        freq=sorted(freq, key= lambda x:x[1], reverse=True)
        L=[]
        for i in range (k):
            L.append(freq[i][0])
        return L
            
