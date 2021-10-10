import random

def BogoSort(arr,n):
    #""shuffles the array if its not organized""
    if(check_sorted(arr,n)==False):
        random.shuffle(arr)
        BogoSort(arr,n)

def check_sorted(arr,n):
    for i in range(0,n-1):
        if(arr[i]>arr[i+1]):
            return False
    return True


arr = [1,4,5,3,2]
n = len(arr)
BogoSort(arr,n)
print("sorted array :"+str(arr))
