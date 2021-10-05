#rotating list elements anticlockwise
def rotate(arr,n,k):
    k = k%n
    for i in range(0,n):
        if i < k:
            print(arr[n+i-k] , end=" ")
        else :
            print(arr[i-k], end = " ")
a = [1,2,3,4,5]
n = len(a)
k = int(input("enter how many time to rotate?"))
rotate(a,n,k)
