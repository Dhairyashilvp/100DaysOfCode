class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        fh = list(s[:int((len(s)/2))])
        sh = list(s[int(len(s)/2):])
        o = t = 0
        print(fh, sh)
        for i in range(len(fh)):
            if fh[i] in v:
                o += 1
            if sh[i] in v:
                t += 1
            if i >
            print(o , " ", t)
        return True if o == t else False
        # vowels = set('aeiouAEIOU')
        # a = b = 0
        # i, j = 0, len(s) - 1
        # while i < j:
        #     a += s[i] in vowels
        #     b += s[j] in vowels
        #     i += 1
        #     j -= 1
        # return a == b