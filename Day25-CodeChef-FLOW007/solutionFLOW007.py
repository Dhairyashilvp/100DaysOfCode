T = int(input())
while T > 0:
    ans = ""
    N = input()
    for n in reversed(range(len(N))):
        if ans:
            ans += N[n]
        else:
            if int(N[n]) > 0:
                ans += N[n]
    print(ans)
    T -= 1