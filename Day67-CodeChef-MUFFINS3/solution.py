T = int(input())
while T > 0:
    ans = 0
    N, B, M = map(int, input().split())
    while N != 0:
        if N % 2 == 0:
            ans += ((N / 2) * M) + B
            N = N / 2
        else:
            ans += (((N + 1) / 2) * M) + B
            N = N - ((N + 1) / 2)
        M = M * 2
    T -= 1
    print(int(ans) - B)