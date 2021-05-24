package main

import "fmt"

const pi = 3.1415

func main() {
	printCircleArea(2)
	printCircleArea(4)

	fmt.Println("Площадь круга с радиусом 5 см =", calculateCircleArea(5))
}

func printCircleArea(radius int) {
	fmt.Printf("Радиус круга: %d см.\n", radius)
	fmt.Println("Формула для расчёта площади круга: A = π·r2")

	circleArea := calculateCircleArea(radius)
	fmt.Printf("Площадь круга: %f32 см.кв.\n", circleArea)
}

func calculateCircleArea(raduis int) float32 {
	return float32(raduis) * float32(raduis) * pi
}
