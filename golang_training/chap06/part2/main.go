package main

import (
	"fmt"
	"storage"
)

func spawnEmployees(s storage.storage) {
	for i := 0; i <= 10; i++ {
		s.insert(employee{id: i})
	}
}

func main() {
	ms := storage.newMemoryStorage()
	ds := storage.newDumbStorage()

	spawnEmployees(ms)
	fmt.Println(ms.get(3))

	spawnEmployees(ds)

}
