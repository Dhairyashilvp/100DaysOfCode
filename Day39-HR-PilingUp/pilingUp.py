# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())
while T > 0 :
  n = int(input())
  arr = []
  top = 0
  arr = list(map(int,input().split()))
  while arr:
    if top == 0:
        if arr[0] >= arr[-1]:
            top = arr[0]
            arr.pop(0)
        elif arr[0] < arr[-1]:
            top = arr[-1]
            arr.pop(-1)
    elif top >= (max(arr[0],arr[-1])):
        if arr[0] >= arr[-1]:
            top = arr[0]
            arr.pop(0)
        elif arr[0] < arr[-1]:
            top = arr[-1]
            arr.pop(-1)
    else:
        print('No')
        break
    if arr:
        pass
    else:
        print("Yes")
        break
  T -= 1
