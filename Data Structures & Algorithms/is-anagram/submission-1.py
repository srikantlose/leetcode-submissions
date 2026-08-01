class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMaps={}
        hashMapt={}
        for i in s:
            if i not in hashMaps:
                hashMaps[i]=1
            else:
                hashMaps[i]+=1
        for i in t:
            if i not in hashMapt:
                hashMapt[i]=1
            else:
                hashMapt[i]+=1
        for i in set(s+t):
            if i in hashMaps and i in hashMapt and hashMaps[i] != hashMapt[i]:
                return False
                break
            elif i not in hashMaps or i not in hashMapt:
                return False
                break
        return True