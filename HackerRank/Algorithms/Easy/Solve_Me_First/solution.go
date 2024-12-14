package main

import "fmt"

func solveMeFirst(a int32, b int32) int32 {
	// Hint: Type return (a+b) below
	return a + b
}

func main() {
	var a, b, res int32
	fmt.Scanf("%v\n%v", &a, &b)
	res = solveMeFirst(a, b)
	fmt.Println(res)
}
