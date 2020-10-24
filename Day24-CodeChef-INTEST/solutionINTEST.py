x, y = input().split()
if(int(x)<(float(y)-0.5) and int(x)%5==0):
    print(float(y)-(int(x)+0.5))
else:
    print(y)