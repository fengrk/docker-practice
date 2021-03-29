package main

import "C"

var (
	count int
)

func init() {
	count = 0
}

//export go_hello
func go_hello(name *C.char) *C.char {
	count += 1

	return C.CString("hello " + C.GoString(name))
}

//export go_call_count
func go_call_count() int {
	return count
}

func main() {
}
