class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        t, f, fi = 3, 5, 15
        for i in range(1,n+1):
            if i == fi:
                ans.append("FizzBuzz")
                t = fi + 3
                f = fi + 5
                fi += 15
            elif i == f:
                ans.append("Buzz")
                f += 5
            elif i == t:
                ans.append("Fizz")
                t += 3
            else:
                ans.append(str(i))
        return ans