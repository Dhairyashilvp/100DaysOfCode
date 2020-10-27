T = int(input())
while T > 0:
    ans = 0
    N = input()
    for n in N:
        ans += int(n)        
    T -= 1
    print(ans)