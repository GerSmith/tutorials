package main

import "fmt"

func main() {
	printType(3)
	printType("интерфесы - это легко")
	printType([]string{"слайсы", "тоже"})
}

func printType(value interface{}) {
	if _, ok := value.(int); ok {
		fmt.Println("тип аргумента int")
	} else if _, ok := value.(string); ok {
		fmt.Println("тип аргумента string")
	} else {
		fmt.Println("тип аргумента не int и не string")
	}
}
