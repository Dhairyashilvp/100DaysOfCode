# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int,input().split())
nel = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
h = 0

for i in nel:
    if i in A:
        h += 1
    if i in B:
        h -= 1
print(h)
