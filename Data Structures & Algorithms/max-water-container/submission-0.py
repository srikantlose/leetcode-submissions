class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L,R=0,len(heights)-1
        max=(R-L)*min(heights[L],heights[R])
        while L<R:
            if (R-(L+1))*min(heights[L+1],heights[R]) > max:
                max=(R-(L+1))*min(heights[L+1],heights[R])
            elif ((R-1)-L)*min(heights[L],heights[R-1]) > max:
                max=((R-1)-L)*min(heights[L],heights[R-1])
            L+=1
            R-=1
        return max
            