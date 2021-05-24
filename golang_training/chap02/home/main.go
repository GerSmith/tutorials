package main

import (
	"errors"
	"fmt"
	"math"
)

func main() {
	// круг
	printCircleArea(2)
	printCircleArea(-2)
	// треугольник
	printTriangleArea(5, 2)
	printTriangleArea(-5, 2)
	printTriangleArea(5, -2)
	printTriangleArea(-5, -2)
	// прямоугольник
	printRectangleArea(2, 5)
	printRectangleArea(-2, 5)
	printRectangleArea(2, -5)
	printRectangleArea(-2, -5)
}

func printCircleArea(radius int) {
	// функция выводит площадь круга по переданному значению радиуса (см)
	// обращаясь к функции calculateCircleArea()
	circleArea, err := calculateCircleArea(radius)

	if err != nil {
		fmt.Println(err.Error())
		return
	}

	fmt.Printf("Радиус круга: %d см.\n", radius)
	fmt.Println("Формула для расчёта площади круга: A = π·r2")

	fmt.Printf("Площадь круга: %f см.кв.\n", circleArea)
}

func calculateCircleArea(radius int) (float32, error) {
	// функция считает площадь круга по переданному значению радиуса (см)
	if radius <= 0 {
		return float32(0), errors.New("радиус круга не может быть отрицательным")
	}

	return float32(radius) * float32(radius) * math.Pi, nil
}

func printTriangleArea(base int, height int) {
	// функция выводит площадь треугольника
	// по переданным значениям основания (см) и высоте (см)
	// обращаясь к функции calculateTriangleArea()
	triangleArea, err := calculateTriangleArea(base, height)

	if err != nil {
		fmt.Println(err.Error())
		return
	}

	fmt.Printf("Основание треугольника: %d см.\n", base)
	fmt.Printf("Высота треугольника: %d см.\n", height)
	fmt.Println("Формула для расчёта площади треугольника: A = 0.5·S·h")

	fmt.Printf("Площадь треугольника: %f см.кв.\n", triangleArea)
}

func calculateTriangleArea(base int, height int) (float32, error) {
	// функция считает площадь треугольника
	// по переданным значениям основания (см) и высоте (см)
	if base <= 0 {
		return float32(0), errors.New("основание треугольника не может быть отрицательным")
	}
	if height <= 0 {
		return float32(0), errors.New("высота треугольника не может быть отрицательной")
	}
	return 0.50 * float32(base) * float32(height), nil
}

func printRectangleArea(sideOne int, sideTwo int) {
	// функция выводит площадь прямоугольника
	// по переданному значению сторон (см)
	// обращаясь к функции calculateRectangleArea()
	rectangleArea, err := calculateRectangleArea(sideOne, sideTwo)

	if err != nil {
		fmt.Println(err.Error())
		return
	}

	fmt.Printf("Стороны прямоугольника: %d и %d см.\n", sideOne, sideTwo)
	fmt.Println("Формула для расчёта площади прямоугольника: A = a·b")

	fmt.Printf("Площадь прямоугольника: %f см.кв.\n", rectangleArea)
}

func calculateRectangleArea(sideOne int, sideTwo int) (float32, error) {
	// функция считает площадь прямоугольника
	// по переданному значению сторон (см)
	if sideOne <= 0 || sideTwo <= 0 {
		return float32(0), errors.New("сторона прямоугольника не может быть отрицательной")
	}

	return float32(sideOne) * float32(sideTwo), nil
}
