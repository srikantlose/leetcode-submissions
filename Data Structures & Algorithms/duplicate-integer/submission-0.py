class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countMap={}
        for i in nums:
            if i not in countMap:
                countMap[i]=1
            else:
                countMap[i]+=1
                return True
                break
                
        return False    
        