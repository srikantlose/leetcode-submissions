class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ridx=len(nums)-k
        L=nums[:ridx]
        nums=nums[ridx:]
        for i in L:
            nums.append(i)
        

        