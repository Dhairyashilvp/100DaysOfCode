T = input()
while(T > 0):
    preety_no = 0
    l = input()
    r = input()
    for i in range(l,r):
        p = i % 10;
        if(p == 2 or p == 3 or p == 9):
            preety_no+=1        
    print(preety_no)
    T-=1