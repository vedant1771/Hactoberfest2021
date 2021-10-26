#Bubble SORT

#BUBBLE SORT FUNCTION
def Bubble_sort(a):
    n=len(a)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]

#ARRAY INPUT
from array import *
a=array('i',[])
m=int(input("Enter length of array: "))
for i in range(m):
    x=int(input("Num: "))
    a.append(x)
#FUNCTION CALL
Bubble_sort(a)
#OUTPUT
print(a)