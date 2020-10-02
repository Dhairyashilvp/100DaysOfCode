from array import *
#[10,20,30,40,50]
#  0  1  2  3  4
arr = array('i', [10,20,30,40,50])

arr.insert(1,60)#inserts the element at given index

for x in arr:
 print(x)
print("-----------------------")
arr.remove(40)#removes the elemnet

for x in arr:
 print(x)
print("-----------------------")
# print(arr.index(40))#will give error as we removed 40 earlier
print(arr.index(30))#Returns indes of given element
print("-----------------------")
arr[2] = 80

for x in arr:
 print(x)