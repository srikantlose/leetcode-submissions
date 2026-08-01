class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L,R,curSum,diff=0,0,0,0
        while R<len(nums):
            curSum+=nums[R]
            if curSum>=target:
                while curSum>=target:
                 diff=R-L
                 curSum-=nums[L]
                 L+=1
            
            R+=1
        if(diff!=0):
            return diff+1
        else:
            return 0
        

