package main

import "fmt"

var vals []int = []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

func main() {
	val := 3
	pos := binarySearch(val, 0, 9)
	fmt.Println(pos)

}

//recursive binary search
func binarySearch(val, low, high int) int {
	mid := int((low + high) / 2)
	if vals[mid] == val {
		return mid
	} else if vals[mid] > val {
		high = mid - 1
	} else {
		low = mid + 1
	}
	return binarySearch(val, low, high)
}
