class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}
        for i in nums:
            if target-i not in hashMap:
                hashMap[i]=1
            elif (target-i in hashMap and i == target-i):
                return[nums.index(target-i),nums.index(i,nums.index(target-i)+1)]
            else:
                return[nums.index(target-i),nums.index(i)]

        