l={}
for i in range(int(input())):
    x=input()
    if x not in l:
        l[x]=1
    else:
        l[x]=l[x]+1
print(len(l))
for i in l:
    print(l[i],end=" ")