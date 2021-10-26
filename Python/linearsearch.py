def linearsearch(arr, n, x):

    for i in range(n):
        if arr[i]==x:
            return i
    return -1

n=int(input("enter the number of element"))
arr=[]
for i in range(n):
    a=int(input())
    arr.append(a)
x=int(input())
result=linearsearch(arr, n, x)
if result==-1:
    print("element not found")
else:
    print("the index of element in array",result)     