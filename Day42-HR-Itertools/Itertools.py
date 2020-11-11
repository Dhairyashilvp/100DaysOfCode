# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
w,l = input().split()
t = list(itertools.permutations(w,int(l)))
t.sort()
for i in t:
    for j in i:
        print(j,end="")
    print()
