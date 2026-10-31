package main

import (
	"fmt"
	"iter"
	"os"
	"strconv"
	"strings"
)

func main() {
	data, _ := os.ReadFile(os.Args[1])
	lines := strings.Split(strings.TrimSpace(string(data)), ",")
	total := 0
	for _, line := range lines {
		interval := ParseInterval(line)
		//fmt.Println(line)
		//fmt.Println(interval.lower, "-", interval.upper)
		for id := range interval.generateIDs() {
			total += id
			fmt.Println(id)
		}
	}
	fmt.Println(total)

}

type Interval struct {
	lower string
	upper string
}

func ParseInterval(s string) *Interval {
	lower, upper, _ := strings.Cut(s, "-")
	return &Interval{lower: lower, upper: upper}
}

// ----------------------------------------
// Only Generate Invalid IDs
// More complicated than just iterating through
// every integer in the range and checking if it is invalid,
// here we explicitly construct all invalid IDs with only
// one extraneous check
// ----------------------------------------
func (i *Interval) generateIDs() iter.Seq[int] {
	return func(yield func(int) bool) {
		n := len(i.lower)
		left := i.lower[:(n+1)/2]
		l, _ := strconv.Atoi(left)
		j, _ := strconv.Atoi(left + left)
		k, _ := strconv.Atoi(i.upper)
		lower, _ := strconv.Atoi(i.lower)
		lastmax := lower
		for j <= k {
			// should only need to do this check once
			if j > lower {
				if !yield(j) {
					return
				}
			}
			l = l + 1
			left = strconv.Itoa(l)
			lastmax = j
			j, _ = strconv.Atoi(left + left)
		}
		right := i.upper[(n+1)/2:]
		upper, _ := strconv.Atoi(i.upper)
		j, _ = strconv.Atoi(right + right)
		for j > lastmax {
			// fails at most once
			if j < upper {
				if !yield(j) {
					return
				}
			}
			l = l - 1
			right = strconv.Itoa(l)
			j, _ = strconv.Atoi(right + right)
		}
	}
}
