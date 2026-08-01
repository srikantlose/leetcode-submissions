class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L=0
        window=set()
        window.add(nums[L])
        for R in range(1,len(nums)-1):
            if nums[R] not in window and abs(L-R)>k:
                window.remove(nums[L])
                L+=1
                window.add(nums[R])
                
            elif nums[R] not in window and abs(L-R)<=k:
                window.add(nums[R])
            else:
                return True
        return False
                
