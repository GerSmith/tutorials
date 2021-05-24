package main

import (
	"fmt"
	"time"
)

func main() {
	start := time.Now()
	fmt.Println("Programm start...")

	time.Sleep(1000 * time.Millisecond)

	stop := time.Now()
	fmt.Printf("Programm stop! The call took %v to run.\n", stop.Sub(start))
}
