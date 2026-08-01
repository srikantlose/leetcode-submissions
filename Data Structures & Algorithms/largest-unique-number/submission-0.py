class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        seen={}
        maxele=-1
        for i in nums:
            if i not in seen:
                seen[i]=1
            else:
                seen[i]+=1
        
        for key,value in seen.items():
            if value==1:
                maxele=max(maxele,key)
        return maxele

        