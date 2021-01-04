class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a = set(allowed)
        na = 0
        for w in words:
            for c in w:
                if c in a:
                    pass
                else:
                    na += 1
                    break
        return len(words) - na   