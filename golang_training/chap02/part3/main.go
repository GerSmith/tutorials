package main

import "fmt"

func main() {
	var p *int

	fmt.Println("Пустой указатель:", p)

	x := 10

	fmt.Println("Значение переменной x:", x)
	fmt.Println("Переменная хранится в", &x)

	increment(&x)

	fmt.Println("Значение x после вызова функции increment():", x)
}

func increment(p *int) {
	*p++
}
