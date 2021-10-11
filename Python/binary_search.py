def binary_search(arr,item):
    begin = 0
    end = len(arr)-1
    while begin<=end:
        mid = begin +(end-begin)//2
        if arr[mid]==item:
            return "{} found at {}".format(item,mid+1)
        elif arr[mid]>item:
            end = mid-1
        else:
            begin = mid+1
    return "{} not found".format(item)
print(binary_search([5,90,234,567,100],567)) 
