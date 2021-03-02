// Variable basics
// Variables may contain a-z, A-Z, and 1-9 and may start with a letter or an underscore
// types include: int, bool, string, float (others not mentioned)


package main

import "fmt"


func main() {

	// single variable definition
	var age int
	fmt.Println("My age is", age)

	// Multiple variable definition - using var keyword you can define a list of variables in this way
	var (
		a int
		b float32
		c bool
		str string
		yesno bool
		fruit string
	)

	// A c-like print statement
	fmt.Printf("a = %d, b = %f", a, b)


	// multiple variables can be initialized in "parallel assignments"
	// items on the right of the '=' are assigned to items on the right in the same order as they appear
	d, e, f = 4, 5, "string"
}









