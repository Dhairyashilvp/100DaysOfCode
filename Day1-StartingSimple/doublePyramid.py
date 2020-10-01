N = 5
l = N-1
a = 1
for h in range(N):
    for x in range(l):
        print("  ",end='')
    for y in range(a):    
        print('* ',end='')
    for p in range(l+l-1):   
        print('  ',end='')
    for q in range(a-1 if h == N-1 else a):   
        print('* ',end='')
    for r in range(l):
        print('  ',end='')
    l = l-1
    a = a + 2
    print()