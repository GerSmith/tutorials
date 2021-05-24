package main

import "fmt"

type employee struct {
	name   string
	sex    string
	age    int
	salary int
}

func newEmployee(name, sex string, age, salary int) employee {
	return employee{
		name:   name,
		sex:    sex,
		age:    age,
		salary: salary,
	}
}

func (e employee) getInfo() string {
	return fmt.Sprintf("Сотрудник: %s\nВозраст: %d\nЗарплата: %d\n", e.name, e.age, e.salary)
}

// func setName(e *employee, name string) {
// e.name = name
// }

func (e *employee) setName(name string) {
	e.name = name
}

func main() {
	employee1 := newEmployee("Вася", "М", 25, 1500)
	employee2 := newEmployee("Дима", "М", 23, 1300)

	fmt.Printf("%s\n", employee1.getInfo())
	fmt.Printf("%s\n", employee2.getInfo())

	// setName(&employee1, "Генадий")
	employee1.setName("Тарас")

	fmt.Printf("%s\n", employee1.getInfo())
	fmt.Printf("%s\n", employee2.getInfo())
}
