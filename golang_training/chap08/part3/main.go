package main

import "fmt"

func main() {
	numbers := make(chan int)

	go generateNumbers(1000, numbers)

	for {
		numbers, ok := <-numbers

		fmt.Println(numbers, ok)

		if !ok {
			break
		}
	}
}

func generateNumbers(n int, res chan int) {
	for i := 0; i <= n; i++ {
		res <- i * 2
	}

	close(res) // без этого будет deadlock
}
