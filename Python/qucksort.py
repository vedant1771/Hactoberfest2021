from array import array
import random
Length=15
def partition(start, end, array):
    pivot_index = start
    pivot = array[pivot_index]
    while start < end:
            while start < len(array) and array[start] <= pivot:
                start += 1
            while array[end] > pivot:
                end -= 1
            
            if(start < end):
                array[start], array[end] = array[end], array[start]
                print(array)
           
    array[end], array[pivot_index] = array[pivot_index], array[end]
    print(array)
    return end
	
def quick_sort(start, end, array):
    if (start < end):
        p = partition(start, end, array)
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)
        
def genrateRandom():
    randomList=[]
    
    # Length=int(input("input enter length of list \n"))
    # start=int(input("enter start of sequence \n"))
    # stop=int(input("enter stop of sequence "))
    for i in range(Length):
        randomList.append(random.randint(10,3000))
        
    print("random sequenc is ",randomList)
    return randomList
		


array=genrateRandom()
quick_sort(0, len(array) - 1,array )

print(f'Sorted array: {array}')
	