class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        freqnew={k:v for v,k in freq.items()}
        L=[]
        keyList=sorted(freqnew.keys(),reverse=True)
        print(keyList)
        for i in range(k):
            L.append(freqnew[keyList[i]])
        return L
