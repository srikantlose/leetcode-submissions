class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L,R=0,len(heights)-1
        maximum=0
        while L<R:
            newmax=(R-L)*min(heights[L],heights[R])
            max1,max2=0,0
            if (R-(L+1))*min(heights[L+1],heights[R]) > newmax:
                max1=(R-(L+1))*min(heights[L+1],heights[R])
            if ((R-1)-L)*min(heights[L],heights[R-1]) > newmax:
                max2=((R-1)-L)*min(heights[L],heights[R-1])
                
            maximum=max(max1,max2,newmax)
            L+=1
            R-=1
            
        return maximum