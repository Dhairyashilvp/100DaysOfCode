N=int(input())
stu_arr = list(list(map(str,input().rstrip().split()))for _ in range(N))
q = input()
t=0
for i in stu_arr:
    if q in i:
        i.remove(q)
        l = len(i)
        for j in i:
            t += float(j)
print("{:.2f}".format(t/float(l)))
# print(stu_arr)