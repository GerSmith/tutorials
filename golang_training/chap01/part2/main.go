package main

import "fmt"

const pi = 3.1415

func main() {
	circleRadius := 2 // радиус круга в сантиметрах
	// площадь круга
	circleArea := float32(circleRadius) * float32(circleRadius) * pi

	fmt.Printf("Радиус круга: %d см.\n", circleRadius)
	fmt.Println("Формула для расчёта площади круга: A = π·r2")
	fmt.Printf("Площадь круга: %f32 см.кв.\n", circleArea)
}
