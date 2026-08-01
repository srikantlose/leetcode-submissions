class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}
        for i in nums:
            if target-i not in hashMap:
                hashMap[i]=1
            else:
                return[nums.index(target-i),nums.index(i)]

        