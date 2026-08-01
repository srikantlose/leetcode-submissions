class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hm={char:idx for idx,char in enumerate(keyboard)}
        time=0
        for i in range(len(word)-1):
            time+=abs(hm[word[i+1]]-hm[word[i]])
        
        return time+hm[word[0]]