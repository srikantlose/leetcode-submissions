class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        L=0
        c=0
        sum=0
        for R in range(len(arr)):
            
            if R-L>k-1:
                sum-=arr[L]
                L+=1
                
            sum+=arr[R]
            c+=1
            if(c>=k):
                average=sum/k
                if(average>=threshold):
                    count+=1
                
        return count