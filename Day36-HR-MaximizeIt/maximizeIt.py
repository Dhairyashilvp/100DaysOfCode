# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
from itertools import product

def maximizeIt(arr,M):
    # print(arr)
    ret = map(lambda x: sum(i**2 for i in x)%M ,product(*arr))
           
    return max(ret)
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    K,M = map(int, input().rstrip().split())
    arr = []
    for _ in range(K):
        arr.append(list(map(int, input().split()))[1:])

    result = maximizeIt(arr, M)
    fptr.write(str(result) + '\n')
    fptr.close()
