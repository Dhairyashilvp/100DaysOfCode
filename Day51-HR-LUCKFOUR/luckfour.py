T = input()
a = 0
count = 0
while(T>0):
    a = input()
    s= str(a)
    for i in range(len(s)):
        p = s[i]
        if p == '4':
            count+=1
    count = 0
    T-=1
