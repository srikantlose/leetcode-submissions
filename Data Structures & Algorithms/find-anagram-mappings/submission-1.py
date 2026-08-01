class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm={}
        for i in nums1:
            hm[i]=nums2.index(i)
        L=[]
        for i in hm.values():
            L.append(i)
        return L