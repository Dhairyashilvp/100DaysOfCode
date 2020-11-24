T = input()
while(T > 0):
    S = None
    sum = 0
    S = input()
    for i in range(len(S)):
        c = S[i]
        if(c.isnumeric()):
            sum = int(c) if sum == 0 else sum + int(c)
    print(sum)
    T -= 1