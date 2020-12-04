T = int(input())
while T > 0:
    ans = 0
    n, k = map(int,input().split())
    l = list(map(int, input().split()))
    print(int(sum(l) / k) + 1)
    T -= 1