package main

import (
	"fmt"
	"math"
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

func (d *Dial) rotate(steps int) int {
	return ((((d.state + steps) % d.max) + d.max) % d.max)
}

func (d *Dial) Turn(steps int) {
	d.state = d.rotate(steps)
}

// ----------------------------------------
// ZeroCrosses returns fully crossing zero, not landing on it
// ----------------------------------------
func (d *Dial) ZeroCrosses(steps int) int {
	rndtrips := int(math.Abs(float64(steps))) / d.max
	old := d.state
	new := d.rotate(steps)
	if old < new && steps < 0 || old > new && steps > 0 {
		if new != 0 && old != 0 {
			rndtrips++
		}
	}
	return rndtrips
}

func (d *Dial) Zero() bool {
	return d.state == 0
}

func parse(dir string) int {
	sign := -1
	if dir[0] == 'R' {
		sign = 1
	}
	steps, _ := strconv.Atoi(dir[1:])
	steps = sign * steps
	return steps
}

func main() {
	dial := NewDial(50, 100)
	count := 0
	data, _ := os.ReadFile(os.Args[1])
	lines := strings.Split(strings.TrimSpace(string(data)), "\n")
	for _, line := range lines {
		steps := parse(line)
		rndtrips := dial.ZeroCrosses(steps)
		count += rndtrips
		dial.Turn(steps)
		if dial.Zero() {
			count++
		}
	}
	fmt.Println(count)
}
