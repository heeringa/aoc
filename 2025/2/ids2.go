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
		for id := range interval.generateIDs() {
			total += id
			//fmt.Println(id)
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
// Siightly more complicated than just iterating through
// every integer in the range and checking if it is invalid,
// here we explicitly construct all invalid IDs with only
// one extraneous check.
// ----------------------------------------
func (i *Interval) generateIDs() iter.Seq[int] {

	check := func(i int) bool {
		s := strconv.Itoa(i)

		for j := 1; j <= len(s)/2; j += 1 {
			pattern := s[:j]
			found := true
			for k := j; k < len(s); k += j {
				m := min(len(s), k+j)
				if s[k:m] != pattern {
					found = false
					break
				} else {
				}
			}
			if found {
				return true
			}
		}
		return false
	}

	return func(yield func(int) bool) {
		lower, _ := strconv.Atoi(i.lower)
		upper, _ := strconv.Atoi(i.upper)
		for j := lower; j <= upper; j++ {
			if check(j) {
				if !yield(j) {
					return
				}
			}
		}
	}
}
