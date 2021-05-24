package main

import (
	"fmt"
	"time"
)

func main() {
	t := time.Now() // время старта

	fmt.Printf("Старт: %s\n", t.Format(time.RFC3339))

	go func() {
		for {
			for _, r := range `-\|/` {
				fmt.Printf("\r%c", r)
				time.Sleep(time.Millisecond * 100)
			}
		}
	}()

	// очень сложные вычисления
	go calculateSomething(1000)
	// а эти вычисления ещё сложнее
	// go calculateSomething(2000)
	calculateSomething(2000)

	// блокирует выполнение главной горутины
	// time.Sleep(9 * time.Second)

	fmt.Printf("Время выполения программы: %s\n", time.Since(t))
}

func calculateSomething(n int) {
	t := time.Now()

	result := 0
	for i := 0; i <= n; i++ {
		result += i * 2
		time.Sleep(time.Millisecond * 3)
	}

	fmt.Printf("Результат: %d; Прошло времени: %s\n", result, time.Since(t))
}
