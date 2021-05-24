package main

import "fmt"

func main() {
	todoList := []string{
		"купить хлеб",
		"купить молоко",
		"купить масло",
		"купить шоколадку",
	}

	fmt.Println("Длина списка до:", len(todoList))
	fmt.Println("Емкость списка до:", cap(todoList))

	// for index, item := range todoList {
	// fmt.Printf("%d. %s\n", index+1, item)
	// }

	todoList = append(todoList, "идти домой", "пинать опавшую листву")

	fmt.Println("Длина списка после:", len(todoList))
	fmt.Println("Емкость списка после:", cap(todoList))

	newTodoList := append(todoList, "пышь-пышь", "фьють-фьють")

	fmt.Printf("Длина = %d и емкость = %d у старого среза\n", len(todoList), cap(todoList))
	fmt.Printf("Длина = %d и емкость = %d у нового среза\n", len(newTodoList), cap(newTodoList))
}
