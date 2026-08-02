class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        idx=0
        for char in s:
            if idx < len(t) and char == t[idx]:
                idx += 1
        return len(t[idx:])