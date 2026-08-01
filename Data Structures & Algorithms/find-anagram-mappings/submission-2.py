class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        L=[]
        for i in nums1:
            L.append(nums2.index(i))
        return L