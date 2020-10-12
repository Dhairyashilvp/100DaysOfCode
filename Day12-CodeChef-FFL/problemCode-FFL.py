# cook your dish here
T = int(input())

while T > 0 :
    c = 0
    d = []
    f = []
    flag = 0
    ip = input()
    N,S = ip.split()
    mm = 100 - int(S)
    
    ip1 = input()
    n1 = ip1.split()

    ip2 = input()
    n2 = ip2.split()

    for v in n2:
        if int(v) == 0:
            d.append(n1[c])
            c += 1
        elif int(v) == 1:
            f.append(n1[c])
            c += 1
        else:
            pass
    for value in d:
        for val in f:
            if int(value) + int(val) <= mm:
                flag = 1
                break
            else:
                pass
    if flag == 1:
        print("yes")
    else:
        print("no")
    T -= 1