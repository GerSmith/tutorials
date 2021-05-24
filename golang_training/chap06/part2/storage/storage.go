package storage

import (
	"errors"
	"fmt"
)

type Employee struct {
	id     int
	name   string
	age    string
	salary int
}

type Storage interface {
	Insert(e Employee) error      // вставка
	Get(id int) (Employee, error) // получение данных
	Delete(id int) error          //удаление
}

type MemoryStorage struct {
	data map[int]Employee
}

type DumbStorage struct{}

func NewMemoryStorage() *MemoryStorage {
	return &MemoryStorage{
		data: make(map[int]Employee),
	}
}

func (s *MemoryStorage) Insert(e Employee) error {
	s.data[e.id] = e

	return nil
}

func (s *MemoryStorage) Get(id int) (Employee, error) {
	e, exists := s.data[id]
	if !exists {
		return Employee{}, errors.New("Employee with such id doesn't exist")
	}

	return e, nil
}

func (s *MemoryStorage) Delete(id int) error {
	Delete(s.data, id)
	return nil
}

func newDumbStorage() *DumbStorage {
	return &DumbStorage{}
}

func (s *DumbStorage) Insert(e Employee) error {
	fmt.Printf("вставка пользователя с id: %d прошла успешно\n", e.id)
	return nil
}

func (s *DumbStorage) Get(id int) (Employee, error) {
	e := Employee{
		id: id,
	}

	return e, nil
}

func (s *DumbStorage) Delete(id int) error {
	fmt.Printf("вставка пользователя с id: %d прошла успешно\n", id)
	return nil
}

func main() {
	var s Storage

	fmt.Println("s = nil", s == nil)
	fmt.Printf("type of s: %T\n\n", s)

	s = NewMemoryStorage()

	fmt.Println("s == nil", s == nil)
	fmt.Printf("type of s: %T\n\n", s)

	s = newDumbStorage()

	fmt.Println("s:", s)
	fmt.Printf("type of s: %T\n\n", s)

	s = nil

	fmt.Println("s:", s)
	fmt.Printf("type of s: %T\n\n", s)

	ms := NewMemoryStorage()
	ds := newDumbStorage()

}
