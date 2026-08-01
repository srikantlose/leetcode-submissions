class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L,R=0,len(heights)-1
        maximum=0
        while L<R:
            newmax=(R-L)*min(heights[L],heights[R])
            if newmax > maximum:
                maximum = newmax
            
            if heights[L] < heights[R]:
                L+=1
            else:
                R-=1
            
        return maximum