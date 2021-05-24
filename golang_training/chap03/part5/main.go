package main

import "fmt"

func main() {
	todoList := [4]string{
		"купить хлеб",
		"купить молоко",
		"купить масло",
		"купить шоколадку",
	}

	var tasks []string
	fmt.Println(tasks == nil)

	tasks = todoList[1:4]
	fmt.Println(tasks == nil)

	for index := range tasks {
		fmt.Println(tasks[index])
	}

	todoList[3] = "сделать ДЗ по прошлым урокам"
	fmt.Println("-------- ПОСЛЕ ИЗМЕНЕНИЯ todoList --------")

	for index := range tasks {
		fmt.Println(tasks[index])
	}

	fmt.Println("-------- ПОСЛЕ ИЗМЕНЕНИЯ changeTasks(tasks) --------")
	changeTasks(tasks)

	for index := range tasks {
		fmt.Println(tasks[index])
	}
}

func changeTasks(tasks []string) {
	tasks[0] = "пройти курс по GO"
	tasks[1] = "сказать автору спасибо :)"
}
