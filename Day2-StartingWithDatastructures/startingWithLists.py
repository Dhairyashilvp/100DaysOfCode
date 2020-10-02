l1 = ['physics', 'chemistry', 1997, 2000]
l2 = [1, 2, 3, 4, 5, 6, 7 ]
print( "l1: ", l1[0])#this will print element at index 0
print( "l2: ", l2[1:5])#this will print from index 1 to 4
print("--------------------")
print(l1)
l1[2] = 2001
print(l1)
print("--------------------")
print(l2)
del l2[2]
print(l2)
print("--------------------")
#Basic operations
print(len(l1))#prints length
print(l1+l2)#concatnation
print(l1*2)#Repetition
print(3 in l2)#false as we deleted 3
print(4 in l2)#true
for x in l2: print(x,end=" ")#iteration