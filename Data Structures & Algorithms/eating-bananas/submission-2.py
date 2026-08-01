class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L,R=1,max(piles)
        hours=0
        result=float('inf')
        while L<=R:
            hours=0
            mid=(L+R)//2
            for i in piles:
                hours+=math.ceil(i/mid)
                if hours>h:
                    L=mid+1
                    break
            if hours<=h:
                R=mid-1
                result=min(result,mid)

        return result
