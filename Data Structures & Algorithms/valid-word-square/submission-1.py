class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        minLength=float('inf')
        for i in words:
            minLength=min(minLength,len(i))
        for i in range(min(len(words),minLength)):
            j=i
            check=words[i][j]==words[j][i]
            if check== False:
                break
        return check