t = int(input())	
n = 0
while(t > 0):
    out =   1
    n = input()
    for i in range(2, n):
        out = out * i
    print(out)
    t-=1