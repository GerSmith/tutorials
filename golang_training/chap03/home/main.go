package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println("Переворачиваем все элементы списка")
	someslice := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

	fmt.Println("Базовый список:")
	printSliceItems(someslice)
	fmt.Println("Переворачиваем...")
	replaceSliceContents(someslice)
	fmt.Println("Новый список:")
	printSliceItems(someslice)

	fmt.Println("Выводим числа от 2^1 до 2^n")
	n := 10

	for i := 0; i <= n; i++ {
		fmt.Printf("2^%d = %.1f\n", i, math.Pow(2, float64(i)))
	}

}

func replaceSliceContents(someslice []int) []int {
	for i := len(someslice)/2 - 1; i >= 0; i-- {
		opp := len(someslice) - 1 - i
		someslice[i], someslice[opp] = someslice[opp], someslice[i]
	}
	return someslice
}

func printSliceItems(someslice []int) {
	fmt.Print("[")
	for _, item := range someslice {
		fmt.Printf("%d, ", item)
	}
	fmt.Print("]")
}
