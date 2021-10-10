package main

import "fmt"

type node struct {
	val  int
	next *node
}

func (n *node) listLen() int {
	l := 0
	if n != nil {
		nxtptr := n.next
		for {
			l++
			if nxtptr == nil {
				break
			}
			nxtptr = nxtptr.next
		}
	}
	return l
}

func (n *node) appendVals(vals ...int) *node {
	for _, val := range vals {
		nd := &node{
			val,
			nil,
		}
		if n != nil {
			curptr := n
			nxtptr := curptr.next
			for {
				if nxtptr == nil {
					curptr.next = nd
					break
				}
				curptr = curptr.next
				nxtptr = curptr.next
			}
		} else {
			n = nd
		}
	}
	return n
}

func (n *node) prependVals(vals ...int) *node {
	for _, val := range vals {
		nd := &node{
			val,
			n,
		}
		n = nd
	}
	return n
}

func (n *node) toSlice() []int {
	slice := []int{}
	var nxtptr *node = n
	for {
		if nxtptr == nil {
			break
		}
		slice = append(slice, nxtptr.val)
		nxtptr = nxtptr.next
	}
	return slice
}

func main() {
	var list *node = nil
	list = list.appendVals(5, 6, 7, 8)
	list = list.prependVals(1, 2, 3, 4)
	fmt.Println(list.toSlice())
	fmt.Println(list.listLen())
}
