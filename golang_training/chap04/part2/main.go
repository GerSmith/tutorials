package main

import "fmt"

func main() {
	fmt.Println("Работа со структурами")

	employee := struct {
		name   string
		sex    string // пол
		age    int
		salary int // зарплата
	}{
		name:   "Вася",
		sex:    "М",
		age:    25,
		salary: 1500,
	}

	fmt.Printf("%+v\n", employee)
}
