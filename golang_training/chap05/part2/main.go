package main

import "fmt"

func main() {
	printType(3)
	printType("интерфесы - это легко")
	printType(3.33)
	printType([]string{"слайсы", "тоже"})
}

func printType(value interface{}) {
	switch value.(type) {
	case int:
		fmt.Println("тип аргумента int")
	case string:
		fmt.Println("тип аргумента string")
	case float32:
		fmt.Println("тип аргумента float32")
	case float64:
		fmt.Println("тип аргумента float64")
	default:
		fmt.Println("тип аргумента не int, не string и не float")
	}
}
