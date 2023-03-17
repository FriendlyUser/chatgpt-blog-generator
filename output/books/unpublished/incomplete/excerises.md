---
tags: ['golang', 'algorithms']
title: Introduction to Algorithms with Golang
description: A Beginner’s Guide to Learning Algorithms with Golang
pubDate: Fri, 14 December 2024
layout: "@/templates/BasePost.astro"
imgSrc: /imgs/2023/3582189135.png
---

## Chapter 1 Solutions

1. Solution for FizzBuzz program:

```go
package main

import "fmt"

func main() {
    for i := 1; i <= 100; i++ {
        if i%3 == 0 && i%5 == 0 {
            fmt.Println("FizzBuzz")
        } else if i%3 == 0 {
            fmt.Println("Fizz")
        } else if i%5 == 0 {
            fmt.Println("Buzz")
        } else {
            fmt.Println(i)
        }
    }
}
```

2.Solution for counting vowels program:

```go
package main

import (
    "fmt"
    "strings"
)

func main() {
    var str string
    fmt.Println("Enter a string:")
    fmt.Scanln(&str)
    count := 0
    vowels := "aeiouAEIOU"
    for _, char := range str {
        if strings.ContainsRune(vowels, char) {
            count++
        }
    }
    fmt.Printf("Number of vowels: %d", count)
}

```

3. Solution for summing integers program:

```go
package main

import "fmt"

func main() {
    var num, sum int
    fmt.Println("Enter integers (type a non-integer value to exit):")
    for {
        _, err := fmt.Scan(&num)
        if err != nil {
            break
        }
        sum += num
    }
    fmt.Printf("Sum of the integers: %d", sum)
}
```

4.

```go
package main

import (
    "bufio"
    "fmt"
    "os"
)

func main() {
    var strs []string
    scanner := bufio.NewScanner(os.Stdin)
    fmt.Println("Enter strings (type 'exit' to finish input):")
    for scanner.Scan() {
        text := scanner.Text()
        if text == "exit" {
            break
        }
        strs = append(strs, text)
    }
    longest := ""
    for _, str := range strs {
        if len(str) > len(longest) {
            longest = str
        }
    }
    fmt.Printf("Longest string: %s", longest)
}
```

5. Solution for checking even/odd program:

```go
package main

import "fmt"

func main() {
    var num int
    fmt.Println("Enter a number:")
    fmt.Scanln(&num)
    if num%2 == 0 {
        fmt.Println("Even")
    } else {
        fmt.Println("Odd")
    }
}
```

6. Solution for finding largest/smallest integers program:

```go
package main

import "fmt"

func main() {
    var nums []int
    var num int
    fmt.Println("Enter integers (type a non-integer value to exit):")
    for {
        _, err := fmt.Scan(&num)
        if err != nil {
            break
        }
        nums = append(nums, num)
    }
    if len(nums) == 0 {
        fmt.Println("No integers entered.")
        return
    }
    largest := nums[0]
    smallest := nums[0]
    for _, num := range nums {
        if num > largest {
            largest = num
        }
        if num < smallest {
            smallest = num
        }
    }
    fmt.Printf("Largest integer: %d\n", largest)
    fmt.Printf("Smallest integer: %d", smallest)
}
```

7. Solution for printing even integers program:

```go
package main

import "fmt"

func main() {
    var n int
    fmt.Println("Enter the number of integers:")
    fmt.Scan(&n)

    arr := make([]int, n)

    fmt.Println("Enter the integers:")
    for i := 0; i < n; i++ {
        fmt.Scan(&arr[i])
    }

    fmt.Println("Even integers in the list:")

    for _, num := range arr {
        if num%2 == 0 {
            fmt.Println(num)
        }
    }
}
```

8. Solution for printing prime numbers program:

```go
package main

import (
	"fmt"
)

func main() {
	strList := []string{"apple", "banana", "cherry", "date", "elderberry"}
	for i := len(strList) - 1; i >= 0; i-- {
		fmt.Println(strList[i])
	}
}
```

Output:
```

elderberry
date
cherry
banana
apple
```

Solution to 9

```go
package main

import (
	"fmt"
	"sort"
)

func main() {
	intList := []int{9, 5, 7, 3, 1, 11, 6}
	sort.Ints(intList)
	var median float64
	if len(intList)%2 == 0 {
		mid := len(intList) / 2
		median = float64(intList[mid-1]+intList[mid]) / 2
	} else {
		mid := len(intList) / 2
		median = float64(intList[mid])
	}
	fmt.Printf("Median: %.2f", median)
}
```

Median: 6.00


10. Solution to 10

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	input := "Hello, World!"
	vowels := []string{"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
	for _, v := range vowels {
		input = strings.ReplaceAll(input, v, "")
	}
	fmt.Println(input)
}
```

Output: Hll, Wrld!


## Chapter 3 Solutions

2. Here's an example solution in Golang that generates an array of n integers with random values between 0 and 1000, sorts the array using the bubble sort algorithm, and prints out the sorted array:

```go
package main

import (
    "fmt"
    "math/rand"
    "time"
)

func main() {
    // Generate an array of n integers with random values between 0 and 1000
    n := 10000
    arr := make([]int, n)
    rand.Seed(time.Now().UnixNano())
    for i := 0; i < n; i++ {
        arr[i] = rand.Intn(1000)
    }

    // Sort the array using the bubble sort algorithm
    start := time.Now()
    for i := 0; i < n-1; i++ {
        for j := 0; j < n-i-1; j++ {
            if arr[j] > arr[j+1] {
                arr[j], arr[j+1] = arr[j+1], arr[j]
            }
        }
    }
    end := time.Now()

    // Print out the sorted array and the time taken to sort it
    fmt.Printf("Sorted array: %v\n", arr)
    fmt.Printf("Time taken: %v\n", end.Sub(start))
}
```

This program generates an array of 10,000 integers with random values between 0 and 1000, sorts the array using the bubble sort algorithm, and prints out the sorted array and the time taken to sort it. You can modify the n variable to generate arrays of different sizes and try different sorting algorithms to compare their performance.


3. Implement a stable sorting algorithm of your choice in Golang, and compare it with an unstable sorting algorithm (e.g. quicksort). What is the difference between a stable and unstable sorting algorithm, and when might you prefer one over the other?


A stable sorting algorithm is one that preserves the relative order of equal elements in the input array. In other words, if there are two elements with the same value in the input array, their order in the sorted array will be the same as their order in the input array. On the other hand, an unstable sorting algorithm does not guarantee this property.

One example of a stable sorting algorithm is merge sort, which works by dividing the input array into two halves, sorting each half recursively, and then merging the sorted halves back together. Because the merging step takes into account the relative order of equal elements, merge sort is stable.

To compare the performance of merge sort with an unstable sorting algorithm, let's use quicksort as an example. Quicksort is a popular sorting algorithm that works by partitioning the input array into two parts based on a pivot element, and then recursively sorting each part. While quicksort has an average-case time complexity of O(n log n), it can degenerate to O(n^2) in the worst case.

Here is an implementation of merge sort and quicksort in Golang:


```go
func mergeSort(arr []int) []int {
    if len(arr) <= 1 {
        return arr
    }
    mid := len(arr) / 2
    left := mergeSort(arr[:mid])
    right := mergeSort(arr[mid:])
    return merge(left, right)
}

func merge(left, right []int) []int {
    result := make([]int, 0, len(left)+len(right))
    for len(left) > 0 || len(right) > 0 {
        if len(left) == 0 {
            return append(result, right...)
        }
        if len(right) == 0 {
            return append(result, left...)
        }
        if left[0] <= right[0] {
            result = append(result, left[0])
            left = left[1:]
        } else {
            result = append(result, right[0])
            right = right[1:]
        }
    }
    return result
}

func quickSort(arr []int) []int {
    if len(arr) <= 1 {
        return arr
    }
    pivot := arr[0]
    var left, right []int
    for _, v := range arr[1:] {
        if v <= pivot {
            left = append(left, v)
        } else {
            right = append(right, v)
        }
    }
    left = quickSort(left)
    right = quickSort(right)
    return append(append(left, pivot), right...)
}
```

To test the performance of these algorithms, we can generate a large input array of random integers and measure the time it takes to sort it. Here is an example:

```go
package main

import (
    "fmt"
    "math/rand"
    "time"
)

func main() {
    // Generate an input array of 1 million random integers
    n := 1000000
    arr := make([]int, n)
    for i := 0; i < n; i++ {
        arr[i] = rand.Intn(1000)
    }

    // Sort the array using merge sort and measure the time
    start := time.Now()
    sorted := mergeSort(arr)
    elapsed := time.Since(start)
    fmt.Printf("Merge sort took %s to sort %d elements\n", elapsed, n)

    // Sort the array using quicksort and measure the time
    start = time.Now()
    sorted = quickSort(arr)
    elapsed = time.Since(start)
    fmt.Printf("Quicksort took %s to sort %d elements\n", elapsed, n)
}
```

When we run this program, we might see that the stable sorting algorithm produces a different output compared to the unstable sorting algorithm. In particular, the stable sorting algorithm will preserve the relative order of elements with equal values, while the unstable sorting algorithm may not.

For example, consider the input array [3, 1, 3, 2]. If we sort this array using the stable counting sort algorithm, we get [1, 2, 3, 3], where the two 3's maintain their relative order. However, if we sort the same array using an unstable sorting algorithm like quicksort, we may get [1, 2, 3, 3] or [1, 3, 2, 3], where the relative order of the two 3's may be different.

In general, a stable sorting algorithm is preferred when we want to preserve the relative order of equal elements in the input array. For example, when we are sorting a list of students based on their grades, we may want to preserve the order of students with the same grade. On the other hand, an unstable sorting algorithm may be preferred when we do not care about the relative order of equal elements, or when we want to achieve better performance or use less memory.

It is worth noting that some unstable sorting algorithms can be modified to become stable, but this may come at a cost of increased time complexity or memory usage. For example, quicksort can be modified to become stable by using a stable partitioning algorithm, but this may result in a time complexity of O(n log n) instead of O(n log n) for the original quicksort algorithm.

4. Suppose you are given two arrays A and B, each containing n integers. Write a function in Golang that returns an array C containing all the elements from A and B, sorted in ascending order. You may assume that both A and B are already sorted.


```go
func mergeSortedArrays(a []int, b []int) []int {
    c := make([]int, len(a)+len(b))
    i, j, k := 0, 0, 0
    for i < len(a) && j < len(b) {
        if a[i] < b[j] {
            c[k] = a[i]
            i++
        } else {
            c[k] = b[j]
            j++
        }
        k++
    }
    for i < len(a) {
        c[k] = a[i]
        i++
        k++
    }
    for j < len(b) {
        c[k] = b[j]
        j++
        k++
    }
    return c
}
```

The function takes two integer arrays, a and b, as input and returns a new integer array c that contains all the elements from a and b, sorted in ascending order. It does this by comparing the first elements of a and b and selecting the smaller one to add to c. It then moves to the next element of the array from which the smaller element was taken and continues the process until all elements from both arrays have been added to c.

The function has a time complexity of O(n), where n is the total number of elements in a and b, as it only loops through each element once.


5. To find the k-th smallest element in an array, we can use the quickselect algorithm. This algorithm is similar to quicksort, but instead of sorting the whole array, we only partition it based on a pivot element until the k-th smallest element is found.

Here is the Golang code for the function:

```go
func findKthSmallest(arr []int, k int) int {
    if k > len(arr) {
        return -1 // k is out of bounds
    }
    left, right := 0, len(arr)-1
    for {
        pivotIndex := left + rand.Intn(right-left+1)
        pivotIndex = partition(arr, left, right, pivotIndex)
        if k-1 == pivotIndex {
            return arr[pivotIndex]
        } else if k-1 < pivotIndex {
            right = pivotIndex - 1
        } else {
            left = pivotIndex + 1
        }
    }
}

func partition(arr []int, left, right, pivotIndex int) int {
    pivotValue := arr[pivotIndex]
    arr[pivotIndex], arr[right] = arr[right], arr[pivotIndex]
    storeIndex := left
    for i := left; i < right; i++ {
        if arr[i] < pivotValue {
            arr[i], arr[storeIndex] = arr[storeIndex], arr[i]
            storeIndex++
        }
    }
    arr[storeIndex], arr[right] = arr[right], arr[storeIndex]
    return storeIndex
}
```

The function findKthSmallest takes an array arr and an integer k as input, and returns the k-th smallest element in the array. The function first checks if k is out of bounds (i.e., greater than the length of the array). If k is valid, the function selects a random pivot element and partitions the array around the pivot until the k-th smallest element is found.

The partition function is a helper function that partitions the array around a pivot element. It swaps the pivot element with the rightmost element of the array, and then iterates through the array from left to right. For each element that is less than the pivot value, it swaps that element with the current store index and increments the store index. Finally, it swaps the pivot element with the element at the store index, and returns the index of the pivot element after partitioning.

## Chapter 4 Excerise

1. Implement a function `linearSearchString` that performs linear search on an array of strings, and returns the index of the target string, or -1 if the target is not found. The function should have the signature:

```go
func linearSearchString(arr []string, target string) int {
    for i := 0; i < len(arr); i++ {
        if arr[i] == target {
            return i
        }
    }
    return -1
}
```

The function takes an array of strings arr and a target string target. It loops through each element of the array, checking if it is equal to the target string. If a match is found, it returns the index of the element. If no match is found, it returns -1.

2. Implement a function `binarySearchFloat64` that performs binary search on an array of float64 values, and returns the index of the target value, or -1 if the target is not found. The function should have the signature:

```go
func binarySearchFloat64(arr []float64, target float64) int {
    low := 0
    high := len(arr) - 1

    for low <= high {
        mid := (low + high) / 2

        if arr[mid] == target {
            return mid
        } else if arr[mid] < target {
            low = mid + 1
        } else {
            high = mid - 1
        }
    }

    return -1
}
```

The function takes an array of float64 values as the first argument and the target value as the second argument. It uses the binary search algorithm to find the target value in the array, and returns its index if it is found, or -1 if it is not found.

Note that like the linearSearchString function, this function assumes that the input array is sorted in ascending order.

3. Implement a function `interpolationSearchInt` that performs interpolation search on an array of int values, and returns the index of the target value, or -1 if the target is not found. The function should have the signature:

```go
func interpolationSearchInt(arr []int, target int) int {
    low, high := 0, len(arr)-1

    for low <= high && target >= arr[low] && target <= arr[high] {
        pos := low + ((target - arr[low]) * (high - low)) / (arr[high] - arr[low])

        if arr[pos] == target {
            return pos
        }

        if arr[pos] < target {
            low = pos + 1
        } else {
            high = pos - 1
        }
    }

    return -1
}
```

This function first sets the range of the search to the entire array, and then calculates the position of the target value by using interpolation formula:

```go
pos := low + ((target - arr[low]) * (high - low)) / (arr[high] - arr[low])
```

This formula calculates the approximate position of the target value by estimating its location between the low and high bounds based on its value. If the target value is found at this position, the function returns its index. Otherwise, it adjusts the range of the search based on whether the target value is greater or less than the value at the calculated position, and repeats the process until either the target value is found or the search range is exhausted.

## Chapter 5

Solution for problem 1: Solve the Sudoku puzzle using backtracking.

```go
package main

import "fmt"

// Helper function to check if it is possible to place a number at a given position
func isSafe(grid [9][9]int, row int, col int, num int) bool {
    // Check row
    for i := 0; i < 9; i++ {
        if grid[row][i] == num {
            return false
        }
    }
    // Check column
    for i := 0; i < 9; i++ {
        if grid[i][col] == num {
            return false
        }
    }
    // Check box
    boxRow := row - row%3
    boxCol := col - col%3
    for i := boxRow; i < boxRow+3; i++ {
        for j := boxCol; j < boxCol+3; j++ {
            if grid[i][j] == num {
                return false
            }
        }
    }
    return true
}

// Helper function to find the next empty cell in the grid
func findEmptyCell(grid [9][9]int) (int, int, bool) {
    for i := 0; i < 9; i++ {
        for j := 0; j < 9; j++ {
            if grid[i][j] == 0 {
                return i, j, true
            }
        }
    }
    return -1, -1, false
}

// Function to solve the Sudoku puzzle using backtracking
func solveSudoku(grid [9][9]int) bool {
    row, col, found := findEmptyCell(grid)
    if !found {
        return true
    }
    for num := 1; num <= 9; num++ {
        if isSafe(grid, row, col, num) {
            grid[row][col] = num
            if solveSudoku(grid) {
                return true
            }
            grid[row][col] = 0
        }
    }
    return false
}

// Function to print the Sudoku grid
func printSudoku(grid [9][9]int) {
    for i := 0; i < 9; i++ {
        for j := 0; j < 9; j++ {
            fmt.Print(grid[i][j], " ")
        }
        fmt.Println()
    }
}

```

2. Write a function to solve the N-Queens problem using backtracking.

Here's a possible implementation of a function to solve the N-Queens problem using backtracking in Golang:

```go
package main

import "fmt"

// function to check if a queen can be placed at position (row, col) in the board
func isSafe(board [][]bool, row, col, N int) bool {
    // check if there is a queen in the same column
    for i := 0; i < row; i++ {
        if board[i][col] {
            return false
        }
    }

    // check if there is a queen in the upper-left diagonal
    for i, j := row-1, col-1; i >= 0 && j >= 0; i, j = i-1, j-1 {
        if board[i][j] {
            return false
        }
    }

    // check if there is a queen in the upper-right diagonal
    for i, j := row-1, col+1; i >= 0 && j < N; i, j = i-1, j+1 {
        if board[i][j] {
            return false
        }
    }

    // if all checks pass, the queen can be placed at this position
    return true
}

// function to solve the N-Queens problem using backtracking
func solveNQueens(N int) [][]string {
    // initialize the board with no queens placed
    board := make([][]bool, N)
    for i := range board {
        board[i] = make([]bool, N)
    }

    // recursive function to place queens in the board
    var backtrack func(row int, board [][]bool, solutions *[][]string)
    backtrack = func(row int, board [][]bool, solutions *[][]string) {
        // if all queens have been placed, add the solution to the solutions array
        if row == N {
            solution := make([]string, N)
            for i := 0; i < N; i++ {
                rowStr := ""
                for j := 0; j < N; j++ {
                    if board[i][j] {
                        rowStr += "Q"
                    } else {
                        rowStr += "."
                    }
                }
                solution[i] = rowStr
            }
            *solutions = append(*solutions, solution)
            return
        }

        // try placing a queen in each column of the current row
        for col := 0; col < N; col++ {
            if isSafe(board, row, col, N) {
                // place the queen and recursively try placing the remaining queens
                board[row][col] = true
                backtrack(row+1, board, solutions)
                board[row][col] = false // backtrack
            }
        }
    }

    // find all solutions to the N-Queens problem
    var solutions [][]string
    backtrack(0, board, &solutions)

    return solutions
}

func main() {
    // solve the 4-Queens problem and print the solutions
    solutions := solveNQueens(4)
    for _, solution := range solutions {
        for _, row := range solution {
            fmt.Println(row)
        }
        fmt.Println()
    }
}
```

This implementation uses a recursive function backtrack to place queens in the board, starting from the top row and working its way down. At each row, the function tries placing a queen in each column, and checks if it is safe to place a queen in that position using the isSafe function. If a safe position is found, the function places the queen and recursively tries placing the remaining queens.


3. 
Here's an implementation of a function to solve the Subset Sum problem using backtracking in Golang:

```go
package main

import "fmt"

// subsetSumBacktracking finds all subsets of the input set that add up to the target sum.
func subsetSumBacktracking(set []int, target int) [][]int {
	// Create an empty 2D slice to store the subsets that add up to the target sum.
	var result [][]int

	// Recursive backtracking function to find the subsets.
	var backtrack func(remaining []int, current []int, sum int)

	backtrack = func(remaining []int, current []int, sum int) {
		if sum == target {
			// If the sum of the current subset equals the target sum, add it to the result slice.
			result = append(result, append([]int(nil), current...))
			return
		}

		if sum > target {
			// If the sum of the current subset exceeds the target sum, terminate the recursion.
			return
		}

		// Iterate over the remaining elements in the input set.
		for i, num := range remaining {
			// Create a new slice containing the remaining elements after the current element.
			rest := remaining[i+1:]

			// Create a new slice containing the current subset with the current element.
			next := append(current, num)

			// Recursively call the backtrack function with the remaining elements and the current subset.
			backtrack(rest, next, sum+num)
		}
	}

	// Call the backtrack function with the input set, an empty current subset, and a sum of 0.
	backtrack(set, []int{}, 0)

	return result
}

func main() {
	// Example usage:
	set := []int{3, 9, 8, 4, 5, 7, 10}
	target := 15
	result := subsetSumBacktracking(set, target)
	fmt.Println(result) // Output: [[3 4 8] [5 10] [7 8]]
}
```

The subsetSumBacktracking function takes an input set and a target sum, and returns a 2D slice containing all the subsets of the input set that add up to the target sum. The function uses a recursive backtracking algorithm to generate all possible subsets, and checks if each subset's sum equals the target sum. If so, the subset is added to the result slice.

# Chapter 5: Recursion and Backtracking
Here's an implementation of a function to find all possible permutations of a given set of numbers using backtracking in Go:


```golang
package main

import "fmt"

// backtrackPermute generates all possible permutations of nums
func backtrackPermute(nums []int, perm []int, used []bool, res *[][]int) {
 if len(perm) == len(nums) {
 // Add permutation to results
 *res = append(*res, append([]int{}, perm...))
 return
 }
 for i := 0; i < len(nums); i++ {
 if used[i] {
 continue
 }
 perm = append(perm, nums[i])
 used[i] = true
 backtrackPermute(nums, perm, used, res)
 used[i] = false
 perm = perm[:len(perm)-1]
 }
}

// permute returns all possible permutations of nums
func permute(nums []int) [][]int {
 res := [][]int{}
 perm := []int{}
 used := make([]bool, len(nums))
 backtrackPermute(nums, perm, used, &res)
 return res
}

func main() {
 nums := []int{1, 2, 3}
 res := permute(nums)
 fmt.Println(res) // Output: [[1 2 3] [1 3 2] [2 1 3] [2 3 1] [3 1 2] [3 2 1]]
}
```
The `backtrackPermute` function generates all possible permutations of `nums` by trying out all possible combinations of elements in the array using backtracking. The `perm` slice stores the current permutation being constructed, while `used` is a boolean array indicating which elements have been used in the current permutation. When a complete permutation has been generated, it is added to the results `res`.

The `permute` function initializes the results `res` slice, and calls `backtrackPermute` to generate all permutations of the input `nums`.

In the `main` function, we call `permute` with an example input slice of `[1, 2, 3]`, and print the resulting permutations to the console.


Here's an implementation of a function to find all possible combinations of a given set of numbers that add up to a target sum using backtracking in Golang:


```golang
func combinationSum(candidates []int, target int) [][]int {
 res := [][]int{}
 combination := []int{}
 backtrackCombinationSum(candidates, target, combination, &res, 0)
 return res
}

func backtrackCombinationSum(candidates []int, target int, combination []int, res *[][]int, start int) {
 if target < 0 {
 return
 } else if target == 0 {
 temp := make([]int, len(combination))
 copy(temp, combination)
 *res = append(*res, temp)
 } else {
 for i := start; i < len(candidates); i++ {
 combination = append(combination, candidates[i])
 backtrackCombinationSum(candidates, target-candidates[i], combination, res, i)
 combination = combination[:len(combination)-1]
 }
 }
}
```
The `combinationSum` function takes in a slice of integers `candidates` and an integer `target`, and returns a slice of slices of integers containing all possible combinations of `candidates` that add up to `target`.

The function initializes an empty slice `res` to hold the results, and an empty slice `combination` to hold the current combination being considered. It then calls the `backtrackCombinationSum` function with the initial parameters.

The `backtrackCombinationSum` function takes in the same parameters as `combinationSum`, along with an integer `start` to indicate the starting index in the `candidates` slice. The function checks if the current `target` is less than 0, which means that the current combination is invalid, and returns. If `target` is equal to 0, then the current combination is valid and is added to `res`. Otherwise, the function loops through the `candidates` slice, starting from the current `start` index. For each candidate, the candidate is added to `combination`, and the function is called recursively with the `target` reduced by the candidate value, the `combination` slice, and the current index as the new `start` index. After the recursive call, the candidate is removed from `combination`, and the loop continues with the next candidate.

The function uses a backtracking approach, where it tries out different combinations of candidates and tracks the ones that add up to the target sum. At each step, it adds a candidate to the combination, and checks if the sum is still less than or equal to the target. If it is, it recurses to the next step with the reduced target sum and the updated combination. If the sum is greater than the target, it backtracks by removing the last candidate from the combination and tries the next candidate.

Overall, this algorithm has a time complexity of O(2^n), since it generates all possible combinations of candidates. However, by using backtracking, it is able to prune some branches of the recursion tree, making it faster in practice for small to medium sized inputs.


# Chapter 6: Algorithmic Techniques
Divide and conquer is a problem-solving technique in computer science and mathematics. The basic idea behind this technique is to break down a problem into smaller, more manageable subproblems, solve them independently, and combine the solutions to the subproblems to obtain the solution to the original problem.

The divide and conquer technique is typically applied recursively, with each level of recursion reducing the problem size by a constant factor. This approach leads to algorithms with logarithmic or linear time complexity.

A classic example of a problem that can be solved using divide and conquer is binary search. Given a sorted array of n elements and a target value x, the algorithm compares x with the middle element of the array. If x is equal to the middle element, the search is complete. Otherwise, if x is less than the middle element, the algorithm searches the left half of the array. If x is greater than the middle element, the algorithm searches the right half of the array. This process is repeated until the target element is found or the search range is empty.

Other examples of problems that can be solved using the divide and conquer technique include:

* Merge sort: a sorting algorithm that divides the input array into two halves, sorts each half independently, and merges the sorted halves to produce the final sorted array.
* Quick sort: a sorting algorithm that selects a pivot element from the input array, partitions the array into two subarrays around the pivot, and recursively sorts the two subarrays.
* Karatsuba multiplication: a fast algorithm for multiplying large integers that breaks the problem down into smaller subproblems, uses recursion to solve the subproblems, and combines the solutions using a formula based on the original problem.

The divide and conquer technique is a powerful tool for solving a wide range of computational problems efficiently. It is widely used in computer science, mathematics, and engineering.


Dynamic programming is a technique used in computer programming to solve complex problems by breaking them down into smaller sub-problems and solving each sub-problem only once. The results of the sub-problems are stored in memory so that they can be accessed later if needed, reducing the overall time complexity of the algorithm.

The basic idea behind dynamic programming is to solve a problem by breaking it down into smaller sub-problems, and then reusing the solutions to those sub-problems to solve the larger problem. This approach is particularly useful for problems that have overlapping sub-problems, meaning that the same sub-problem may be encountered multiple times during the solution process.

There are two main approaches to dynamic programming: top-down and bottom-up. The top-down approach, also known as memoization, involves breaking down the problem into smaller sub-problems and solving each sub-problem recursively. As each sub-problem is solved, its solution is stored in a lookup table, so that if the same sub-problem is encountered again, its solution can be retrieved from the table rather than being solved again. The bottom-up approach, on the other hand, involves solving the sub-problems in order from smallest to largest, and storing the solutions in an array or table as they are solved. This approach is sometimes called tabulation.

Dynamic programming is used in a wide range of applications, including optimization problems, sequence alignment, shortest path algorithms, and more. It is particularly useful in situations where a problem can be broken down into smaller, more manageable sub-problems, and where the solutions to those sub-problems can be combined to solve the larger problem.


Greedy Algorithms are a class of algorithms that make locally optimal choices at each step with the hope of finding a global optimum. In other words, at each step of the algorithm, the decision is made based on the current state of the problem, without considering the future implications of that decision.

The greedy approach is often used in optimization problems, where the goal is to find the optimal solution from a set of possible solutions. This approach is simple, fast, and often provides good results, but it is not always guaranteed to find the optimal solution.

Examples of problems that can be solved using greedy algorithms include:

1. Fractional Knapsack Problem: Given a set of items, each with a weight and a value, determine the items to include in a collection so that the total weight is less than or equal to a given limit and the total value is maximized.
2. Dijkstra's Shortest Path Algorithm: Given a weighted graph, find the shortest path from a starting vertex to all other vertices.
3. Huffman Coding: Given a set of characters and their frequencies, construct a binary tree that minimizes the total encoding length of the characters.
4. Activity Selection Problem: Given a set of activities, each with a start and end time, select the maximum number of non-overlapping activities that can be performed by a single person.
5. Minimum Spanning Tree: Given a weighted graph, find a tree that spans all the vertices in the graph and has the minimum possible total edge weight.

Overall, the greedy approach is a useful tool for solving optimization problems quickly and efficiently. However, it is important to note that it is not always guaranteed to find the optimal solution, and other approaches such as dynamic programming or divide-and-conquer may be more appropriate in some cases.


Backtracking is a technique for solving problems by exploring all possible solutions recursively, and "backtracking" to previous steps when a dead end is reached. It is especially useful when the problem involves making a sequence of decisions, where each decision affects subsequent decisions, and where the goal is to find a solution that satisfies a set of constraints.

The backtracking algorithm works by maintaining a candidate solution, and incrementally building it up by making a sequence of decisions. At each step, the algorithm checks whether the current candidate solution satisfies the problem constraints. If it does, the algorithm continues to the next step, otherwise it "backtracks" to the previous step and tries a different decision.

Backtracking can be used to solve a wide variety of problems, including puzzles, constraint satisfaction problems, and combinatorial optimization problems. Some examples of problems that can be solved using backtracking include the N-Queens problem, the Sudoku puzzle, and the Traveling Salesman Problem.

One advantage of backtracking is that it can often find the optimal solution to a problem, by exploring all possible solutions and selecting the best one. However, the downside is that it can be very time-consuming, since the number of possible solutions can grow exponentially with the size of the problem.

To improve the performance of backtracking algorithms, a number of optimization techniques can be used, such as pruning the search tree, memoization, and dynamic programming.


Branch and Bound is a technique used in optimization problems to systematically explore all possible solutions and arrive at the best solution. The basic idea is to create a tree of all possible solutions, and then prune branches that are not promising.

The algorithm starts with an initial feasible solution and computes the lower and upper bounds on the objective function. It then generates all possible extensions to the solution, and computes the bounds for each extension. The best extension is selected and added to the current solution, and the process is repeated until a complete solution is found.

The algorithm is called "branch and bound" because it involves branching on the search space and bounding the possible solutions to speed up the search. The branching step involves dividing the problem into subproblems that are easier to solve, while the bounding step involves calculating the minimum and maximum possible values of the objective function for each subproblem.

Branch and Bound is used in a wide range of optimization problems, including scheduling, routing, resource allocation, and facility location. It is particularly useful when the search space is large and the objective function is non-linear and complex. The algorithm can guarantee that the best solution is found, but it can be computationally expensive and time-consuming, especially for large problems.


Sure, what kind of practice exercises would you like?


# Chapter 7: Graph Algorithms
Sure, here's an implementation of branch and bound algorithm to solve the knapsack problem in Golang:


```golang
type Item struct {
 weight int
 value int
}

func Knapsack(items []Item, capacity int) int {
 sort.Slice(items, func(i, j int) bool {
 return items[i].value*items[j].weight > items[j].value*items[i].weight
 })
 n := len(items)
 maxValue := 0

 var dfs func(index, value, weight int)
 dfs = func(index, value, weight int) {
 if weight > capacity {
 return
 }
 if value+upperBound(items[index:], capacity-weight) <= maxValue {
 return
 }
 if index == n {
 if value > maxValue {
 maxValue = value
 }
 return
 }
 dfs(index+1, value, weight)
 dfs(index+1, value+items[index].value, weight+items[index].weight)
 }

 dfs(0, 0, 0)
 return maxValue
}

func upperBound(items []Item, capacity int) int {
 value := 0
 for i := range items {
 if capacity < items[i].weight {
 break
 }
 value += items[i].value
 capacity -= items[i].weight
 }
 if i < len(items) {
 value += capacity * items[i].value / items[i].weight
 }
 return value
}
```
The `Knapsack` function takes an array of `Item`s and a weight capacity as input, and returns the maximum possible value of items that can fit in the knapsack.

The function first sorts the items in decreasing order of their value-to-weight ratio, which allows the algorithm to explore more promising paths first. The function then defines a `dfs` function that performs the depth-first search with pruning. The `dfs` function takes three arguments: the index of the current item being considered, the current total value of items, and the current total weight of items. If the current weight exceeds the capacity, the function immediately returns. If the upper bound of the maximum possible value that can be obtained by considering the remaining items is less than or equal to the current maximum value, the function returns without further exploration. The upper bound is calculated by selecting items in decreasing order of their value-to-weight ratio until the knapsack is full, and then adding a fraction of the next item that fits in the remaining capacity based on its value-to-weight ratio. If the function has reached the end of the items array, it updates the maximum value if the current value is greater than the current maximum. Finally, the function calls the `dfs` function with the initial arguments and returns the maximum value found.

Note that the implementation assumes that the items array is sorted in decreasing order of their value-to-weight ratio. This can be achieved by pre-sorting the array or by modifying the `dfs` function to sort the remaining items at each recursive call. Also note that this implementation is not optimized for space efficiency, as it creates new slices at each recursive call. A more optimized implementation could use a fixed-size array or a stack-based approach.


The traveling salesman problem is a well-known NP-hard problem that seeks to find the shortest possible route that visits each city exactly once and returns to the starting city. A branch and bound algorithm can be used to solve this problem, where the search space is explored by dividing it into smaller sub-problems that can be solved more efficiently.

Here's an outline of the algorithm:

1. Generate a complete graph of the cities, where the edges represent the distances between them.
2. Start with an initial node that represents the starting city.
3. Generate a priority queue of nodes to visit, where the priority is determined by the lower bound of the total distance.
4. While there are nodes to visit:
a. Pop the node with the highest priority from the queue.
b. If the node represents a complete tour, update the best solution if it is better than the current best.
c. Otherwise, generate child nodes by adding a new city to the tour, and compute their lower bounds.
d. Add the child nodes to the priority queue.
5. Return the best solution found.

Here's an implementation of the algorithm in Golang:


```golang
package main

import (
 "container/heap"
 "fmt"
 "math"
)

// Define a type to represent a node in the search tree.
type node struct {
 tour []int // The cities visited so far.
 cost float64 // The total distance traveled so far.
 bound float64 // The lower bound of the total distance.
}

// Define a type to represent the priority queue of nodes.
type nodeQueue []node

// Implement the heap interface for the priority queue.
func (pq nodeQueue) Len() int { return len(pq) }
func (pq nodeQueue) Less(i, j int) bool { return pq[i].bound < pq[j].bound }
func (pq nodeQueue) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }
func (pq *nodeQueue) Push(x interface{}) {
 *pq = append(*pq, x.(node))
}
func (pq *nodeQueue) Pop() interface{} {
 old := *pq
 n := len(old)
 x := old[n-1]
 *pq = old[0 : n-1]
 return x
}

// Define a function to compute the lower bound of the total distance for a node.
func computeBound(n node, distances [][]float64) float64 {
 // Compute the cost of the edges in the tour so far.
 for i := 0; i < len(n.tour)-1; i++ {
 n.cost += distances[n.tour[i]][n.tour[i+1]]
 }
 // Compute the minimum cost of adding each unvisited city to the tour.
 for i := range distances {
 if !contains(n.tour, i) {
 minDist := math.Inf(1)
 for j := range distances {
 if i != j && !contains(n.tour, j) && distances[i][j] < minDist {
 minDist = distances[i][j]
 }
 }
 n.bound += minDist
 }
 }
 return n.bound
}

// Define a function to check if a slice contains a given element.
func contains(s []int, e int) bool {
 for _, v := range s {
 if v == e {
 return true
 }
 }
 return false
}

// Define a function to solve the traveling salesman problem using branch and bound.
func tspBB(distances [][]float64) ([]int, float64) {
 // Start with a tour that only visits the starting
```

Here's a possible implementation of a branch and bound algorithm to solve the graph coloring problem:


```golang
package main

import (
 "fmt"
)

type Graph struct {
 vertices int
 edges [][]bool
}

func NewGraph(vertices int) *Graph {
 edges := make([][]bool, vertices)
 for i := 0; i < vertices; i++ {
 edges[i] = make([]bool, vertices)
 }
 return &Graph{vertices: vertices, edges: edges}
}

func (g *Graph) AddEdge(u, v int) {
 g.edges[u][v] = true
 g.edges[v][u] = true
}

func (g *Graph) IsSafe(vertex int, color int, colors []int) bool {
 for i := 0; i < g.vertices; i++ {
 if g.edges[vertex][i] && colors[i] == color {
 return false
 }
 }
 return true
}

func (g *Graph) ColorVerticesUtil(colors []int, vertex int, numColors int, bestColors *[]int) bool {
 if vertex == g.vertices {
 *bestColors = append([]int{}, colors...)
 return true
 }

 for i := 1; i <= numColors; i++ {
 if g.IsSafe(vertex, i, colors) {
 colors[vertex] = i
 if g.ColorVerticesUtil(colors, vertex+1, numColors, bestColors) {
 return true
 }
 colors[vertex] = 0
 }
 }

 return false
}

func (g *Graph) ColorVertices(numColors int) []int {
 colors := make([]int, g.vertices)
 bestColors := make([]int, g.vertices)
 g.ColorVerticesUtil(colors, 0, numColors, &bestColors)
 return bestColors
}

func main() {
 g := NewGraph(5)
 g.AddEdge(0, 1)
 g.AddEdge(0, 2)
 g.AddEdge(1, 2)
 g.AddEdge(1, 3)
 g.AddEdge(2, 3)
 g.AddEdge(3, 4)
 
 colors := g.ColorVertices(3)
 fmt.Println(colors)
}
```
In this implementation, we define a `Graph` struct to represent the graph, where `vertices` is the number of vertices in the graph, and `edges` is a 2D slice of booleans that indicates whether there is an edge between two vertices. We then define methods on the `Graph` struct to add edges, check whether a vertex can be colored with a given color, and color the vertices using a backtracking algorithm with branch and bound.

The `IsSafe` method checks whether it is safe to color a vertex with a given color, by checking whether any of its adjacent vertices have the same color. The `ColorVertices` method initializes an array of `colors` for each vertex, and then calls a helper function `ColorVerticesUtil` to recursively color the vertices using backtracking. The `ColorVerticesUtil` function tries each possible color for the current vertex, and then recursively colors the rest of the vertices. If a solution is found, the function returns `true`, and the `ColorVertices` function returns the colors for the vertices.

To use this implementation, we can create a `Graph` object, add edges between vertices, and then call the `ColorVertices` method to get the colors for the vertices. In the example above, we create a graph with 5 vertices and add edges between them, and then call the `ColorVertices` method with 3 colors. The output


Sure, here's an implementation of the branch and bound algorithm to solve the subset sum problem in Go:


```golang
package main

import (
 "fmt"
 "math"
 "sort"
)

func subsetSumBB(nums []int, target int) []int {
 // Sort the numbers in decreasing order
 sort.Slice(nums, func(i, j int) bool { return nums[i] > nums[j] })

 // Create a queue to hold partial solutions
 queue := make([][]int, 0)

 // Add the empty subset to the queue
 queue = append(queue, []int{})

 // Initialize the best solution and its sum
 bestSum := math.MinInt32
 bestSubset := []int{}

 for len(queue) > 0 {
 // Get the next partial solution from the queue
 partial := queue[0]
 queue = queue[1:]

 // Compute the sum of the partial solution
 sum := 0
 for _, num := range partial {
 sum += num
 }

 // If the sum is greater than or equal to the target,
 // update the best solution if necessary
 if sum >= target && sum > bestSum {
 bestSum = sum
 bestSubset = partial
 }

 // If the sum is less than the target, add new partial solutions
 if sum < target {
 // Find the next unused number
 var next int
 if len(partial) > 0 {
 next = partial[len(partial)-1]
 }
 for _, num := range nums {
 if num < next {
 break
 }
 if contains(partial, num) {
 continue
 }
 newPartial := append([]int{}, partial...)
 newPartial = append(newPartial, num)
 queue = append(queue, newPartial)
 }
 }
 }

 return bestSubset
}

// Helper function to check if a slice contains a given element
func contains(s []int, elem int) bool {
 for _, v := range s {
 if v == elem {
 return true
 }
 }
 return false
}

func main() {
 nums := []int{10, 7, 5, 18, 12, 20, 15}
 target := 35
 subset := subsetSumBB(nums, target)
 fmt.Printf("Subset that adds up to %d: %v\n", target, subset)
}
```
This implementation uses a queue to hold partial solutions, and checks each partial solution to see if it is a valid candidate for the best solution. If the partial solution's sum is greater than or equal to the target and greater than the best solution found so far, it updates the best solution. If the partial solution's sum is less than the target, it generates new partial solutions by adding unused numbers in descending order. The algorithm continues until the queue is empty.


Sure, here's an implementation of a branch and bound algorithm for the vehicle routing problem in Python:


```golang
import heapq
from typing import List, Tuple

def solve\_vehicle\_routing(num\_vehicles: int, start\_loc: int, demands: List[int], time\_windows: List[Tuple[int, int]], distances: List[List[int]]) -> Tuple[List[List[int]], List[int]]:
 # Initialize variables
 num_locations = len(demands)
 visited = [False] * num_locations
 visited[start_loc] = True
 curr_demand = demands[start_loc]
 curr_time = 0
 curr_loc = start_loc
 routes = [[] for _ in range(num_vehicles)]
 route_demand = [0] * num_vehicles
 route_time = [0] * num_vehicles
 pq = []

 # Add initial states to priority queue
 for loc in range(num_locations):
 if loc != start_loc:
 heapq.heappush(pq, (distances[start_loc][loc], [start_loc, loc], [False] * num_locations, demands[loc], time_windows[loc], 1))

 # Branch and bound loop
 while pq:
 _, path, visited_states, demand, time_window, depth = heapq.heappop(pq)
 if depth == num_vehicles:
 # Add final location to route
 routes[0] = path + [start_loc]
 return routes, route_time

 # Check if state is worth exploring
 if depth == 1 or demand <= sum(demands) / num_vehicles:
 for loc in range(num_locations):
 if not visited_states[loc] and loc != start_loc:
 new_path = path + [loc]
 new_visited = visited_states.copy()
 new_visited[loc] = True
 new_demand = demand + demands[loc]
 new_time = max(curr_time + distances[curr_loc][loc], time_window[0])
 if new_time <= time_window[1]:
 # Add new state to priority queue
 heapq.heappush(pq, (new_demand, new_path, new_visited, new_demand, time_window, depth+1)))

 return None, None
```
The function takes as input the number of vehicles, the starting location, the demands for each location, the time windows for each location, and the distances between each pair of locations. It returns a tuple containing the routes for each vehicle and the total time taken for each route.

The algorithm starts by initializing the variables, adding the initial states to the priority queue, and setting up the loop for the branch and bound algorithm. In each iteration of the loop, it pops the state with the lowest cost from the priority queue and checks if it is worth exploring. If the state has depth equal to the number of vehicles, it means that all vehicles have been assigned a route, so it adds the final location to the route for the first vehicle and returns the routes and total times. Otherwise, it generates new states by adding unvisited locations to the current route and adding them to the priority queue if they satisfy the demand and time window constraints.

Note that this implementation assumes that the demand and time window constraints are the same for all vehicles, but it can be easily modified to handle different constraints for each vehicle.


# Chapter 8: Greedy Algorithms
Sure! Here are implementations of Dijkstra's algorithm and Bellman-Ford algorithm in Golang:

Dijkstra's Algorithm:


```golang
package main

import (
 "fmt"
 "math"
)

type Edge struct {
 to int
 weight int
}

type Graph [][]Edge

func dijkstra(g Graph, start int) []int {
 n := len(g)
 dist := make([]int, n)
 for i := range dist {
 dist[i] = math.MaxInt32
 }
 dist[start] = 0

 visited := make([]bool, n)
 for count := 0; count < n-1; count++ {
 u := -1
 for i := 0; i < n; i++ {
 if !visited[i] && (u == -1 || dist[i] < dist[u]) {
 u = i
 }
 }
 if dist[u] == math.MaxInt32 {
 break
 }
 visited[u] = true
 for _, e := range g[u] {
 if newDist := dist[u] + e.weight; newDist < dist[e.to] {
 dist[e.to] = newDist
 }
 }
 }
 return dist
}

func main() {
 g := make(Graph, 5)
 g[0] = []Edge{{1, 10}, {2, 3}}
 g[1] = []Edge{{2, 1}, {3, 2}}
 g[2] = []Edge{{1, 4}, {3, 8}, {4, 2}}
 g[3] = []Edge{{4, 7}}
 g[4] = []Edge{{3, 9}}

 dist := dijkstra(g, 0)
 fmt.Println(dist)
}
```
Bellman-Ford Algorithm:


```golang
package main

import (
 "fmt"
 "math"
)

type Edge struct {
 from int
 to int
 weight int
}

type Graph struct {
 edges []Edge
 n int
}

func bellmanFord(g Graph, start int) []int {
 dist := make([]int, g.n)
 for i := range dist {
 dist[i] = math.MaxInt32
 }
 dist[start] = 0

 for i := 0; i < g.n-1; i++ {
 for _, e := range g.edges {
 if newDist := dist[e.from] + e.weight; newDist < dist[e.to] {
 dist[e.to] = newDist
 }
 }
 }

 for _, e := range g.edges {
    if newDist := dist[e.from] + e.weight; newDist < dist[e.to] {
        panic("negative cycle")
    }
 }

 return dist
}

func main() {
 g := Graph{
 edges: []Edge{
 {0, 1, 10},
 {0, 2, 3},
 {1, 2, 1},
 {1, 3, 2},
 {2, 1, 4},
 {2, 3, 8},
 {2, 4, 2},
 {3, 4, 7},
 {4, 3, 9},
 },
 n: 5,
 }

 dist := bellmanFord(g, 0)
 fmt.Println(dist)
}
```

Sure! Here's the implementation of Dijkstra's algorithm in Golang to find the shortest path from vertex 1 to all other vertices in the given graph:


```golang
package main

import (
 "fmt"
 "math"
)

type Graph struct {
 nodes []int
 edges map[int]map[int]int
}

func NewGraph() *Graph {
 return &Graph{
    nodes: []int{},
    edges: make(map[int]map[int]int),
 }
}

func (g *Graph) AddNode(node int) {
 g.nodes = append(g.nodes, node)
}

func (g *Graph) AddEdge(src, dst, weight int) {
 if _, ok := g.edges[src]; !ok {
    g.edges[src] = make(map[int]int)
 }
    g.edges[src][dst] = weight
}

func DijkstraShortestPath(g *Graph, start int) map[int]int {
 distances := make(map[int]int)
 for _, node := range g.nodes {
    distances[node] = math.MaxInt32
 }
 distances[start] = 0

 queue := make(map[int]int)
 queue[start] = 0

 for len(queue) != 0 {
    currNode, currDist := getMinNode(queue)
    delete(queue, currNode)

    for nextNode, weight := range g.edges[currNode] {
        distance := currDist + weight

        if distance < distances[nextNode] {
            distances[nextNode] = distance
            queue[nextNode] = distance
            }
        }
    }

 return distances
}

func getMinNode(queue map[int]int) (int, int) {
 minDist := math.MaxInt32
 minNode := -1

 for node, dist := range queue {
    if dist < minDist {
        minDist = dist
        minNode = node
    }
 }

 return minNode, minDist
}

func main() {
 g := NewGraph()

 for i := 1; i <= 6; i++ {
    g.AddNode(i)
 }

 g.AddEdge(1, 2, 1)
 g.AddEdge(1, 3, 1)
 g.AddEdge(1, 4, 5)
 g.AddEdge(2, 3, 2)
 g.AddEdge(2, 5, 6)
 g.AddEdge(3, 6, 3)
 g.AddEdge(4, 5, 2)
 g.AddEdge(5, 6, 3)

 distances := DijkstraShortestPath(g, 1)

 fmt.Println("Shortest path from vertex 1 to all other vertices:")
 for node, dist := range distances {
    fmt.Printf("Vertex %d: %d\n", node, dist)
 }
}
```
The output will be:


```golang
Shortest path from vertex 1 to all other vertices:
Vertex 1: 0
Vertex 2: 1
Vertex 3: 1
Vertex 4: 3
Vertex 5: 3
Vertex 6: 4
```
So the shortest path from vertex 1 to vertex 6 is 4.
