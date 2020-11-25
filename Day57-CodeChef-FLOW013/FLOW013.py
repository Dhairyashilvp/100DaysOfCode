T = int(input())
p = 0
ari = []
while(T > 0):
    p = 0
    for i in range(3):
        ari[i] = int(input())
    for x in ari:
        p += x
    if(p == 180):
        print("YES")
    else:
        print("NO")
    T -= 1 