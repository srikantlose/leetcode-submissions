class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        hm={}
        flag=0
        flag1=0
        for i in s:
            if i not in hm:
                hm[i]=1
            else:
                hm[i]+=1
        print(hm)
        if len(s)%2==1:
           
            for char,count in hm.items():
                if count%2!=0:
                    flag+=1
                else:
                    continue


                if(flag>1):
                    return False
            return True if flag==1 else False
        else:
            for char,count in hm.items():
                if count%2!=0:
                    flag1=1
            
        return False if flag1==1 else True

