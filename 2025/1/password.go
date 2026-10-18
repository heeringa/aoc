package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

// ----------------------------------------

type Dial struct {
	max   int
	state int
}

func NewDial(state int, max int) *Dial {
	return &Dial{state: state, max: max}
}

func (d *Dial) Turn(steps int) {
	d.state = (d.state + steps) % d.max
}

func (d *Dial) Zero() bool {
	return d.state == 0
}

func main() {
	dial := NewDial(50, 100)
	count := 0
	data, _ := os.ReadFile(os.Args[1])
	lines := strings.Split(strings.TrimSpace(string(data)), "\n")
	for _, line := range lines {
		sign := -1
		if line[0] == 'R' {
			sign = 1
		}
		steps, _ := strconv.Atoi(line[1:])
		steps = sign * steps
		dial.Turn(steps)
		if dial.Zero() {
			count++
		}
	}
	fmt.Println(count)
}
