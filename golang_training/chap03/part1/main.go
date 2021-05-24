package main

import "fmt"

func main() {
	var todoList = [5]string{
		"купить хлеб",
		"купить молоко",
		"купить масло",
	}

	todoList[3] = "купить шоколадку"
	todoList[4] = "идти домой"

	fmt.Printf("Кол-во элементов в списке: %d\n", len(todoList))

	for index, item := range todoList {
		fmt.Printf("%d. %s\n", index, item)
	}

	for index := range todoList {
		fmt.Printf("%d. %s\n", index, todoList[index])
	}

	for _, item := range todoList {
		fmt.Printf("%s\n", item)
	}

}
