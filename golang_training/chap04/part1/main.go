package main

import "fmt"

func main() {
	// var ages map[string]int

	// fmt.Println(ages)
	// fmt.Println("ages == nil", ages == nil)

	// ages := make(map[string]int)
	// ages["Максим"] = 20
	// ages["Олег"] = 24
	// ages["Саня"] = 28

	ages := map[string]int{
		"Максим":    20,
		"Олег":      24,
		"Александр": 28,
		"Антон":     35,
	}

	for key, value := range ages {
		fmt.Printf("%s - %d\n", key, value)
	}

	fmt.Printf("Максиму %d лет\n", ages["Максим"])
	// fmt.Printf("Антону %d лет\n", ages["Антон"])

	ages["Антон"] = 99
	// delete(ages, "Антон")

	age, exists := ages["Антон"]
	if !exists {
		fmt.Println("Антона нет в списке!")
	} else {
		fmt.Printf("Антону %d лет\n", age)
	}

	var ages2 map[string]int

	fmt.Println(ages)
	fmt.Println(ages2)

	ages2 = ages

	delete(ages, "Александр")
	delete(ages, "Олег")

	fmt.Println(ages)
	fmt.Println(ages2)
}
