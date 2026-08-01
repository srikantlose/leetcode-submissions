class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L,R,curSum,diff,flag=0,0,0,0,0
        while R<len(nums):
            curSum+=nums[R]
            if curSum>=target:
                flag=1
                while curSum>=target:
                    
                 diff=R-L
                 curSum-=nums[L]
                 L+=1
            
            R+=1
        if (flag==1):
            return diff+1
        else:
            return 0
        

