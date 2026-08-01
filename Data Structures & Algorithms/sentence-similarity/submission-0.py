class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        for i,j in zip(sentence1,sentence2):
            print([i,j])
            if(i==j):
                continue
            if ([i,j] not in similarPairs) and ([j,i] not in similarPairs):
                return False
        return True