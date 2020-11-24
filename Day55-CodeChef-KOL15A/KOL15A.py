T = input()
name = []; 
while(T>0):
    S = None
    name = None
    S = input()
    name = S.split(" ")
    M = name[0]
    W = name[1]
    j = 0 
    yes = 0
    if(M.length() <= W.length()):
        j = 0
        for i in range(len(W)):
            if(W[i] == M[j]):
                yes+=1
                j+=1
            if(j==len(M)):
                break
    else:
        j = 0
        for i in range(len(M)):
            if(M[i] == W[j]):
                yes += 1 
                j += 1
            if(j==len(W)):
                break
    if(yes == min(len(M),len(W))):
        print("YES")
    else:
        print("NO")
    T-=1