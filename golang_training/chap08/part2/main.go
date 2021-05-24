package main

import (
	"fmt"
	"time"
)

func main() {
	t := time.Now() // время старта

	fmt.Printf("Старт: %s\n", t.Format(time.RFC3339))

	result1 := make(chan int)
	result2 := make(chan int)

	go func() {
		for {
			for _, r := range `-\|/` {
				fmt.Printf("\r%c", r)
				time.Sleep(time.Millisecond * 100)
			}
		}
	}()

	// очень сложные вычисления
	go calculateSomething(1000, result1)

	// а эти вычисления ещё сложнее
	go calculateSomething(2000, result2)

	fmt.Println(<-result1)
	fmt.Println(<-result2)

	fmt.Printf("Время выполения программы: %s\n", time.Since(t))
}

func calculateSomething(n int, res chan int) {
	t := time.Now()

	result := 0
	for i := 0; i <= n; i++ {
		result += i * 2
		time.Sleep(time.Millisecond * 3)
	}

	fmt.Printf("Результат: %d; Прошло времени: %s\n", result, time.Since(t))
	res <- result
}
