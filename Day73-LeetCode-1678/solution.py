class Solution:
    def interpret(self, command: str) -> str:
        def gen(s):
            i = 0
            while i < len(s):
                if s[i] == 'G':
                    i += 1
                    yield 'G'
                elif s[i] == '(' and s[i+1] == ')':
                    i += 2
                    yield 'o'
                else:
                    i += 4
                    yield 'al'

        return ''.join(gen(command))