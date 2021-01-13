class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l = list(sentence.split())
        for i, w in enumerate(l):
            if w.startswith(searchWord):
                return i+1
        return -1