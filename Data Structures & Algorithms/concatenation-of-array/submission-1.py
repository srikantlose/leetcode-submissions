class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        count=0
        n=len(nums)
        ans=[0]*2*n
        for i in nums:
            ans[count]=nums[count]
            ans[count+n]=nums[count]
            count+=1
        return ans