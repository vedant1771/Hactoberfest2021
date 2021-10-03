package main

import "fmt"

// Linear search to detect if value is equal to the values present in list
func linearSearch(list []int, value int) bool {
	for _, item := range list {
		if item == value {
			return true
		}
	}
	return false
}

func main() {
	values := []int{12, 34, 56, 78, 90, 32, 54, 76}
	fmt.Println(linearSearch(values, 90))
}

//P.S - Open terminal and enter 'go run linear_search.go'
