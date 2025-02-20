# Stack & Heap

x= 3
y= x
x= 5
print(x,y)
#output => 5 3

x= [1,2,3,4,5]
y= x
x[:]= [5,4,3,2,1]
x[0]= -1
print(x,y)
#output => [-1,4,3,2,1] [-1,4,3,2,1]


