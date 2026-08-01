class Solution:
    def calPoints(self, operations: List[str]) -> int:
        L=[]
        for i in operations:
            if i not in ["+", "D", "C"]:
                L.append(int(i))
            elif i=="+":
                L.append(L[-1]+L[-2])
            elif i=="C":
                L.pop()
            elif i=="D":
                L.append(L[-1]*2)
        sum_val=0
        for i in L:
            sum_val+=i
        return sum_val