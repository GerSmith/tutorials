package main

import "fmt"

func main() {
	var arr [3]int

	fillArray(arr)

	fmt.Println(arr)
}

func fillArray(arr [3]int) {
	for i := 0; i < len(arr); i++ {
		arr[i] = i
	}

	fmt.Println("fillArray():", arr)
}
