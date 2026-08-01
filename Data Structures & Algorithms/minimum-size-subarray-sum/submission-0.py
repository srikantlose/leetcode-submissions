class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L,R,curSum,count=0,0,0,0
        while R<len(nums):
            curSum+=nums[R]
            if curSum>=target:
                while curSum>=target:
                 count+=1
                 curSum-=nums[L]
                 L+=1
            
            R+=1
        return count

