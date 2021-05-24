package main

import "fmt"

const pi = 3.1415

var globalVar string = "Я глобальная переменная"

func main() {
	var phrase string = "Go рулит!"
	var empty string
	var number int = 1
	var number2 uint = 2
	var number3 float32 = 3.14
	var isGoCool bool = true
	var name string = "Sergey"
	localVar := "я локальная переменная внутри main()"
	fmt.Println(phrase)
	fmt.Println(empty)
	fmt.Println(number)
	fmt.Println(number2)
	fmt.Println(number3)
	fmt.Println(isGoCool)
	fmt.Println(name)
	fmt.Println(globalVar)
	fmt.Println(localVar)
	fmt.Println("Число Пи:", pi)
}
