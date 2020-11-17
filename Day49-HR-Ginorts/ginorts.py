s = list(input())
enum = []
onum = []
cap = []
sc = []
for e in s:
    if e.isdigit():
        if int(e) % 2 == 0:
            enum.append(e)
        else:
            onum.append(e)
    elif e.isupper():
        cap.append(e)
    else:
        sc.append(e)
enum.sort()
onum.sort()
cap.sort()
sc.sort()
ans = ""
print(ans.join(sc) + ans.join(cap) + ans.join(onum) + ans.join(enum))