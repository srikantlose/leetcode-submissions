class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        count=0
        n=length(nums)
        for i in nums:
            ans[i]=nums[i]
            ans[i+n]=nums[i]
        return ans