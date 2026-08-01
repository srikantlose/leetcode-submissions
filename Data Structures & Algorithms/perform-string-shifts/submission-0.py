class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for i in shift:
            arr=list(s)
            
            if i[0]==0:
                L=0
                for i in range(i[1]):
                    arr.append(arr[L])
                    L+=1
                newarr=[]
                for k in range(len(s)):
                    newarr.append(arr[L])
                    L+=1
                s="".join(newarr)
                arr=newarr
            else:
                L=0
                for i in range(i[1]):
                    for j in range(len(s)-1):
                        arr.append(arr[L])
                        L+=1
                newarr=[]
                for k in range(len(s)):
                    newarr.append(arr[L])
                    L+=1
                s="".join(newarr)
                arr=newarr
                print(s)
            
        return(s)
        