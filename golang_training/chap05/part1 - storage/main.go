package main

import (
	"errors"
	"fmt"
)

type employee struct {
	id     int
	name   string
	age    string
	salary int
}

type storage interface {
	insert(e employee) error      // вставка
	get(id int) (employee, error) // получение данных
	delete(id int) error          //удаление
}

type memoryStorage struct {
	data map[int]employee
}

type dumbStorage struct{}

func newMemoryStorage() *memoryStorage {
	return &memoryStorage{
		data: make(map[int]employee),
	}
}

func (s *memoryStorage) insert(e employee) error {
	s.data[e.id] = e

	return nil
}

func (s *memoryStorage) get(id int) (employee, error) {
	e, exists := s.data[id]
	if !exists {
		return employee{}, errors.New("employee with such id doesn't exist")
	}

	return e, nil
}

func (s *memoryStorage) delete(id int) error {
	delete(s.data, id)
	return nil
}

func newDumbStorage() *dumbStorage {
	return &dumbStorage{}
}

func (s *dumbStorage) insert(e employee) error {
	fmt.Printf("вставка пользователя с id: %d прошла успешно\n", e.id)
	return nil
}

func (s *dumbStorage) get(id int) (employee, error) {
	e := employee{
		id: id,
	}

	return e, nil
}

func (s *dumbStorage) delete(id int) error {
	fmt.Printf("вставка пользователя с id: %d прошла успешно\n", id)
	return nil
}

func spawnEmployees(s storage) {
	for i := 0; i <= 10; i++ {
		s.insert(employee{id: i})
	}
}

func main() {
	var s storage

	fmt.Println("s = nil", s == nil)
	fmt.Printf("type of s: %T\n\n", s)

	s = newMemoryStorage()

	fmt.Println("s == nil", s == nil)
	fmt.Printf("type of s: %T\n\n", s)

	s = newDumbStorage()

	fmt.Println("s:", s)
	fmt.Printf("type of s: %T\n\n", s)

	s = nil

	fmt.Println("s:", s)
	fmt.Printf("type of s: %T\n\n", s)

	ms := newMemoryStorage()
	ds := newDumbStorage()

	spawnEmployees(ms)
	fmt.Println(ms.get(3))

	spawnEmployees(ds)

}
