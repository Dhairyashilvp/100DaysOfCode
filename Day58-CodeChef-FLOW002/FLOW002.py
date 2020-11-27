T = int(input())
while T > 0:
    ans = 0
    N = list(map(int, input().split()))
    if N[1] > 0:
       ans = N[0] % N[1] 
    T -= 1
    print(ans)