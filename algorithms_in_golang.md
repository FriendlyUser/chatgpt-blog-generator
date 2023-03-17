---
tags: ['golang', 'algorithms']
title: Introduction to Algorithms with Golang
description: A Beginner’s Guide to Learning Algorithms with Golang
pubDate: Fri, 14 December 2024
layout: "@/templates/BasePost.astro"
imgSrc: /imgs/2023/323056288.png
---
# Chapter 9: Divide and Conquer Algorithms
Solution:

To solve this problem, we can use the Divide and Conquer algorithm. The basic idea is to divide the set of 3D points into two halves, solve the problem recursively in each half, and then merge the solutions.

The merging process involves finding the minimum distance between two points that are split between the two halves and the minimum distance between two points that are entirely in one of the halves.

Here's the Go code implementation:


```golang
type Point struct {
 x, y, z float64
}

func distance(a, b Point) float64 {
 dx, dy, dz := a.x-b.x, a.y-b.y, a.z-b.z
 return math.Sqrt(dx*dx + dy*dy + dz*dz)
}

func min(a, b float64) float64 {
 if a < b {
 return a
 }
 return b
}

func closestPair(points []Point) float64 {
 n := len(points)
 if n < 2 {
 return math.Inf(1)
 }

 mid := n / 2
 left := points[:mid]
 right := points[mid:]

 d := min(closestPair(left), closestPair(right))

 var strip []Point
 for i := range points {
 if math.Abs(points[i].x-points[mid].x) < d {
 strip = append(strip, points[i])
 }
 }

 sort.Slice(strip, func(i, j int) bool {
 return strip[i].y < strip[j].y
 })

 for i := range strip {
 for j := i + 1; j < len(strip) && strip[j].y-strip[i].y < d; j++ {
 d = min(d, distance(strip[i], strip[j]))
 }
 }

 return d
}
```
In the `Point` struct, we represent each point in 3D space with its `x`, `y`, and `z` coordinates. The `distance` function calculates the Euclidean distance between two points. The `min` function returns the minimum of two float64 values.

The `closestPair` function takes a slice of `Point` values as input and returns the minimum distance between any two points in the set. The function first checks if there are fewer than two points in the set and returns positive infinity if there are. The function then divides the set into two halves and solves the problem recursively in each half. The minimum distance `d` is initialized with the minimum of the distances returned by the recursive calls.

The `strip` slice is created to store the points that are within the distance `d` from the splitting plane. This is done by iterating over all points and checking if their `x` coordinates are within distance `d` of the midpoint `x` coordinate. The `strip` slice is then sorted by the `y` coordinate of each point.

The nested `for` loops iterate over all pairs of points in the `strip` slice and calculate the distance between them. The loop continues as long as the difference in `y` coordinates is less than `d`. If the distance between the current pair of points is less than the current minimum distance `d`, then `d` is updated to the new minimum distance.

Overall, this algorithm has a time complexity of O(n log n) and a space complexity of O(n).


Solution:

To solve this problem, we can use the Divide and Conquer algorithm. The basic idea is to divide the rotated sorted array into two halves, and then determine which half contains the minimum element. We can do this by comparing the middle element with the last element of the array. If the middle element is greater than the last element, then the minimum element must be in the second half of the array. Otherwise, the minimum element must be in the first half of the array.

Here's the Go code implementation:


```golang
func findMin(nums []int) int {
 n := len(nums)
 if n == 1 {
 return nums[0]
 }
 if nums[0] < nums[n-1] {
 return nums[0]
 }

 mid := n / 2
 if nums[mid] > nums[n-1] {
 return findMin(nums[mid:])
 } else {
 return findMin(nums[:mid+1])
 }
}
```
The `findMin` function takes a slice of integers as input and returns the minimum element in the rotated sorted array. If the array contains only one element, then that element is the minimum, and the function returns it. Otherwise, if the first element is less than the last element, then the array is not rotated, and the function returns the first element.

Otherwise, we calculate the middle index of the array, and we compare the middle element with the last element of the array. If the middle element is greater than the last element, then the minimum element must be in the second half of the array. We call the `findMin` function recursively on the second half of the array. Otherwise, the minimum element must be in the first half of the array. We call the `findMin` function recursively on the first half of the array.

Overall, this algorithm has a time complexity of O(log n) and a space complexity of O(log n), where n is the size of the array.


Solution:

To solve this problem, we can use the Divide and Conquer algorithm. The basic idea is to divide the given sequence into two halves, and then find the maximum subsequence sum in each half. The maximum subsequence sum can either be entirely in the left half, entirely in the right half, or spanning across both halves. We can find the maximum subsequence sum spanning across both halves by calculating the maximum subsequence sum starting from the middle element and going towards the left, and the maximum subsequence sum starting from the middle element and going towards the right. The maximum subsequence sum spanning across both halves is the sum of these two maximum subsequence sums.

Here's the Go code implementation:


```golang
func maxSubsequenceSum(nums []int) int {
 n := len(nums)
 if n == 1 {
 return nums[0]
 }

 mid := n / 2
 maxLeft := maxSubsequenceSum(nums[:mid])
 maxRight := maxSubsequenceSum(nums[mid:])
 maxCrossing := maxCrossingSum(nums, mid)

 return max(maxLeft, maxRight, maxCrossing)
}

func maxCrossingSum(nums []int, mid int) int {
 leftSum := math.MinInt32
 rightSum := math.MinInt32
 sum := 0

 for i := mid - 1; i >= 0; i-- {
 sum += nums[i]
 if sum > leftSum {
 leftSum = sum
 }
 }

 sum = 0

 for i := mid; i < len(nums); i++ {
 sum += nums[i]
 if sum > rightSum {
 rightSum = sum
 }
 }

 return leftSum + rightSum
}

func max(nums ...int) int {
 res := math.MinInt32
 for _, num := range nums {
 if num > res {
 res = num
 }
 }
 return res
}
```
The `maxSubsequenceSum` function takes a slice of integers as input and returns the maximum sum of a subsequence of the given sequence. If the sequence contains only one element, then that element is the maximum subsequence sum, and the function returns it.

Otherwise, we calculate the middle index of the sequence, and we find the maximum subsequence sum in the left half and in the right half of the sequence recursively. We also find the maximum subsequence sum spanning across both halves by calling the `maxCrossingSum` function.

The `maxCrossingSum` function takes the input sequence and the middle index as input, and returns the maximum subsequence sum spanning across both halves of the sequence. The function iterates from the middle index towards the left and calculates the maximum subsequence sum starting from the middle element and going towards the left. It also iterates from the middle index towards the right and calculates the maximum subsequence sum starting from the middle element and going towards the right. The maximum subsequence sum spanning across both halves is the sum of these two maximum subsequence sums.

Finally, we return the maximum of the maximum subsequence sums in the left half, the right half, and spanning across both halves.

Overall, this algorithm has a time complexity of O(n log n) and a space complexity of O(log n), where n is the size of the sequence.


Solution:

To solve this problem, we can use the Divide and Conquer algorithm known as the "Gift Wrapping" or "Jarvis March" algorithm. The basic idea is to start with the leftmost point in the set and then find the next point that is the farthest counterclockwise from the current point. We keep repeating this process until we reach the starting point, forming a convex hull around the set of points.

Here's the Go code implementation:


```golang
type point struct {
 x, y int
}

func convexHull(points []point) []point {
 n := len(points)
 if n < 3 {
 return nil
 }

 hull := make([]point, 0, n)
 start := 0

 // Find the leftmost point
 for i := 1; i < n; i++ {
 if points[i].x < points[start].x {
 start = i
 }
 }

 current := start
 next := -1

 for {
 hull = append(hull, points[current])

 // Find the next point on the hull
 for i := 0; i < n; i++ {
 if i == current {
 continue
 }
 if next == -1 {
 next = i
 }
 cross := crossProduct(points[i], points[current], points[next])
 if cross < 0 {
 next = i
 } else if cross == 0 {
 if distance(points[current], points[i]) > distance(points[current], points[next]) {
 next = i
 }
 }
 }

 current = next
 next = -1

 if current == start {
 break
 }
 }

 return hull
}

func crossProduct(a, b, c point) int {
 return (b.x-a.x)*(c.y-a.y) - (b.y-a.y)*(c.x-a.x)
}

func distance(a, b point) int {
 dx := a.x - b.x
 dy := a.y - b.y
 return dx*dx + dy*dy
}
```
The `convexHull` function takes a slice of points as input and returns a slice of points representing the convex hull of the input points. If the number of input points is less than 3, then the function returns nil, since a convex hull requires at least 3 points.

We start by finding the leftmost point in the set of input points, which will be the starting point of our convex hull. We initialize an empty slice to hold the points on the hull.

Then we start iterating over the points to find the next point on the hull. For each point, we calculate the cross product between the current point, the next point, and the point being considered. If the cross product is negative, then the point being considered is counterclockwise to the current and next points, so we update the next point to be the point being considered. If the cross product is zero, then the point being considered is collinear with the current and next points, so we update the next point only if the distance between the current point and the point being considered is greater than the distance between the current point and the current next point.

Once we have found the next point on the hull, we add it to the hull and update the current point to be the next point. We repeat this process until we have returned to the starting point, at which point we have completed the convex hull.

The `crossProduct` function takes three points as input and returns the cross product of the vectors formed by the two line segments connecting the points.

The `distance` function takes two points as input and returns the squared


# Chapter 10: String Algorithms
Sure, here's the implementation of the Knuth-Morris-Pratt (KMP) algorithm for string searching in Go:


```golang
func KMPSearch(text, pattern string) int {
 n := len(text)
 m := len(pattern)

 if m == 0 {
 return 0
 }

 if m > n {
 return -1
 }

 // Calculate the prefix function
 prefix := make([]int, m)
 prefix[0] = 0
 j := 0
 for i := 1; i < m; i++ {
 for j > 0 && pattern[j] != pattern[i] {
 j = prefix[j-1]
 }
 if pattern[j] == pattern[i] {
 j++
 }
 prefix[i] = j
 }

 // Use the prefix function to search for the pattern in the text
 j = 0
 for i := 0; i < n; i++ {
 for j > 0 && pattern[j] != text[i] {
 j = prefix[j-1]
 }
 if pattern[j] == text[i] {
 j++
 }
 if j == m {
 return i - m + 1
 }
 }

 return -1
}
```
The `KMPSearch` function takes two strings as input - the text in which to search for the pattern and the pattern to search for - and returns the index of the first occurrence of the pattern in the text, or -1 if the pattern is not found.

The KMP algorithm uses a prefix function to avoid unnecessary backtracking while searching for the pattern. The prefix function is calculated as follows: for each position in the pattern, the length of the longest proper suffix that is also a prefix of the substring up to that position is computed. The prefix function is stored in an array `prefix` of length `m` (the length of the pattern).

To search for the pattern in the text, we initialize two indices `i` and `j` to zero. We iterate over the characters of the text. If the current character matches the current character of the pattern, we increment `j`. If `j` reaches the end of the pattern, we have found a match, so we return the index `i - m + 1` of the start of the match in the text. If the current character of the text does not match the current character of the pattern, we use the prefix function to determine how far back to backtrack `j`. We set `j` to the value of `prefix[j-1]` (the length of the longest proper suffix of the substring up to the previous position that is also a prefix of the pattern). We continue until we reach the end of the text or find a match.

Note that the implementation assumes that the input strings are ASCII strings. If the input strings contain Unicode characters, the implementation will need to be modified to handle multi-byte characters.


Sure, here's an implementation of the Boyer-Moore algorithm for string searching in Go:


```golang
func BoyerMooreSearch(text, pattern string) int {
 n := len(text)
 m := len(pattern)

 if m == 0 {
 return 0
 }

 if m > n {
 return -1
 }

 // Preprocess the pattern
 lastOccurrence := make(map[byte]int)
 for i := 0; i < m; i++ {
 lastOccurrence[pattern[i]] = i
 }

 // Search for the pattern in the text
 i := m - 1
 j := m - 1
 for i < n && j >= 0 {
 if text[i] == pattern[j] {
 i--
 j--
 } else {
 if last, ok := lastOccurrence[text[i]]; ok && last < j {
 i = i + m - 1 - last
 j = m - 1
 } else {
 i = i + m
 j = m - 1
 }
 }
 }

 if j < 0 {
 return i + 1
 } else {
 return -1
 }
}
```
The `BoyerMooreSearch` function takes two strings as input - the text in which to search for the pattern and the pattern to search for - and returns the index of the first occurrence of the pattern in the text, or -1 if the pattern is not found.

The Boyer-Moore algorithm uses two heuristic rules to avoid unnecessary comparisons while searching for the pattern. The first rule is the "bad character rule", which states that if a character in the text does not match the corresponding character in the pattern, we can skip ahead in the text to the next occurrence of that character in the pattern. To implement this rule, we preprocess the pattern to store the index of the last occurrence of each character in the pattern in a hash table `lastOccurrence`.

The second rule is the "good suffix rule", which states that if a suffix of the pattern matches a substring of the text, we can skip ahead in the text to the next occurrence of the next longest suffix of the pattern that matches a substring of the text. To implement this rule, we keep track of two indices `i` and `j`. We start at the end of the pattern (`i = m - 1`, `j = m - 1`) and compare the characters of the pattern and text from right to left. If the characters match, we decrement both indices. If they do not match, we use the bad character rule to determine how far to skip ahead in the text, and we update `i` and `j` accordingly.

We continue until we reach the beginning of the text or find a match. If we find a match, we return the index of the start of the match in the text (`i + 1`). If we reach the beginning of the text without finding a match, we return -1.

Note that this implementation assumes that the input strings are ASCII strings. If the input strings contain Unicode characters, the implementation will need to be modified to handle multi-byte characters.


Sure, here's an implementation of the Rabin-Karp algorithm for string matching in Go:


```golang
func RabinKarpSearch(text, pattern string) int {
 n := len(text)
 m := len(pattern)

 if m == 0 {
 return 0
 }

 if m > n {
 return -1
 }

 // Compute the hash of the pattern
 patternHash := hash(pattern)

 // Search for the pattern in the text
 textHash := hash(text[:m])
 for i := 0; i <= n-m; i++ {
 if textHash == patternHash && text[i:i+m] == pattern {
 return i
 }
 if i < n-m {
 textHash = rehash(text, i, i+m, textHash, m)
 }
 }

 return -1
}

// Computes the hash of a string using the Rabin-Karp hash function
func hash(str string) uint64 {
 var h uint64
 for i := 0; i < len(str); i++ {
 h = (h << 1) + uint64(str[i])
 }
 return h
}

// Computes the hash of a string segment by subtracting the contribution
// of the leftmost character and adding the contribution of the rightmost
// character, using the Rabin-Karp hash function
func rehash(str string, oldIndex, newIndex int, oldHash uint64, patternLen int) uint64 {
 var newHash uint64
 newHash = oldHash - uint64(str[oldIndex])<<(patternLen-1)
 newHash = (newHash << 1) + uint64(str[newIndex])
 return newHash
}
```
The `RabinKarpSearch` function takes two strings as input - the text in which to search for the pattern and the pattern to search for - and returns the index of the first occurrence of the pattern in the text, or -1 if the pattern is not found.

The Rabin-Karp algorithm uses a rolling hash function to efficiently compute the hash value of each substring of the text. We compute the hash of the pattern before searching and use it to compare with the hash of each substring of the text. If the hash values match, we compare the substrings to see if they are actually equal.

The rolling hash function used in this implementation is a simple implementation of the Rabin-Karp hash function, which uses a polynomial hash function to compute the hash value of a string. The hash function is defined as:


```golang
hash(s) = s[0] * x^(n-1) + s[1] * x^(n-2) + ... + s[n-1] * x^0
```
where `s` is the string, `n` is the length of the string, and `x` is a constant chosen to be a large prime number.

To compute the hash of each substring of the text, we use a rolling hash function that subtracts the contribution of the leftmost character of the current substring and adds the contribution of the rightmost character of the next substring, as shown in the `rehash` function.

Note that this implementation assumes that the input strings are ASCII strings. If the input strings contain Unicode characters, the implementation will need to be modified to handle multi-byte characters.


Sure, here's an implementation of the Ukkonen's algorithm for building a suffix tree in Go:


```golang
type Node struct {
 Edges map[byte]*Edge
 Suffix *Node
 Start int
 End *int
}

type Edge struct {
 Start *int
 End *int
 Node *Node
}

func BuildSuffixTree(s string) *Node {
 n := len(s)
 root := &Node{Edges: make(map[byte]*Edge)}

 // Build the tree one character at a time
 activeNode := root
 activeEdge := 0
 activeLength := 0
 remainder := 0
 lastNewNode := root
 for i := 0; i < n; i++ {
 lastNewNode = nil
 remainder++
 for remainder > 0 {
 if activeLength == 0 {
 activeEdge = i
 }
 edge, ok := activeNode.Edges[s[activeEdge]]
 if !ok {
 // Create a new leaf node and edge
 leaf := &Node{Edges: make(map[byte]*Edge), Start: i}
 edge = &Edge{Start: &i, End: nil, Node: leaf}
 activeNode.Edges[s[activeEdge]] = edge
 addSuffixLink(lastNewNode, activeNode)
 lastNewNode = nil
 } else {
 // Walk down the edge as far as possible
 j := *edge.Start
 if activeLength >= *edge.End-j {
 activeEdge += *edge.End - j
 activeLength -= *edge.End - j
 activeNode = edge.Node
 continue
 }
 if s[*edge.Start+activeLength] == s[i] {
 // The current suffix already exists in the tree
 activeLength++
 addSuffixLink(lastNewNode, activeNode)
 lastNewNode = nil
 break
 }
 // Split the edge and create a new leaf node
 splitEnd := *edge.Start + activeLength
 splitNode := &Node{Edges: make(map[byte]*Edge), Start: *edge.Start, End: &splitEnd}
 splitEdge := &Edge{Start: edge.Start, End: &splitEnd, Node: splitNode}
 activeNode.Edges[s[activeEdge]] = splitEdge
 leaf := &Node{Edges: make(map[byte]*Edge), Start: i}
 leafEdge := &Edge{Start: &i, End: nil, Node: leaf}
 splitNode.Edges[s[i]] = leafEdge
 edge.Start = &splitEnd
 edge.Node = splitNode
 addSuffixLink(lastNewNode, splitNode)
 lastNewNode = splitNode
 }
 remainder--
 if activeNode == root && activeLength > 0 {
 activeLength--
 activeEdge = i - remainder + 1
 } else {
 activeNode = activeNode.Suffix
 }
 }
 }

 return root
}

// Adds a suffix link from the last new internal node to the specified node
func addSuffixLink(lastNewNode, node \*Node) {
 if lastNewNode != nil {
 lastNewNode.Suffix = node
 }
}
```
The `BuildSuffixTree` function takes a string as input and returns the root node of the suffix tree for the string.

The implementation uses Ukkonen's algorithm to build the suffix tree one character at a time. The algorithm maintains an active point that is initially set to the root of the tree. For each character in the string, the algorithm either adds


Sure, here's an implementation of finding all occurrences of a pattern in a given string using suffix tree algorithm in Go:


```golang
type Node struct {
 Edges map[byte]*Edge
 Suffix *Node
 Start int
 End *int
}

type Edge struct {
 Start *int
 End *int
 Node *Node
}

// Finds all occurrences of a pattern in a string using a suffix tree
func FindAllOccurrences(s, pattern string) []int {
 n := len(s)
 root := buildSuffixTree(s)

 // Walk down the tree to find the nodes corresponding to the pattern
 nodes := []*Node{root}
 for i := 0; i < len(pattern); i++ {
 var nextNodes []*Node
 for _, node := range nodes {
 if edge, ok := node.Edges[pattern[i]]; ok {
 nextNodes = append(nextNodes, edge.Node)
 }
 }
 nodes = nextNodes
 }

 // Collect the positions of the pattern in the string
 var positions []int
 for _, node := range nodes {
 collectPositions(node, n-len(pattern), &positions)
 }
 sort.Ints(positions)

 return positions
}

// Builds a suffix tree for the given string
func buildSuffixTree(s string) *Node {
 // Implementation omitted for brevity
}

// Recursively collects the positions of the leaves below the given node
func collectPositions(node \*Node, offset int, positions \*[]int) {
 if node.End != nil {
 *positions = append(*positions, *node.End-offset)
 }
 for _, edge := range node.Edges {
 collectPositions(edge.Node, offset, positions)
 }
}
```
The `FindAllOccurrences` function takes two strings as input, `s` and `pattern`, and returns a slice of integers representing the positions in `s` where the pattern occurs.

The implementation first builds a suffix tree for the string `s` using the `buildSuffixTree` function (omitted for brevity). Then it walks down the tree to find the nodes corresponding to the pattern. Finally, it collects the positions of the leaves below these nodes and returns them as a sorted slice of integers.

Note that this implementation assumes that the pattern is non-empty and that it occurs at least once in the string. It also assumes that the string and the pattern consist only of ASCII characters.


Sure, here's an implementation of the Longest Common Subsequence (LCS) problem using dynamic programming in Go:


```golang
// Finds the length of the longest common subsequence of two strings using dynamic programming
func LongestCommonSubsequenceLength(s1, s2 string) int {
 m, n := len(s1), len(s2)
 dp := make([][]int, m+1)
 for i := range dp {
 dp[i] = make([]int, n+1)
 }

 for i := 1; i <= m; i++ {
 for j := 1; j <= n; j++ {
 if s1[i-1] == s2[j-1] {
 dp[i][j] = dp[i-1][j-1] + 1
 } else {
 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
 }
 }
 }

 return dp[m][n]
}

// Returns the maximum of two integers
func max(a, b int) int {
 if a > b {
 return a
 }
 return b
}
```
The `LongestCommonSubsequenceLength` function takes two strings as input, `s1` and `s2`, and returns an integer representing the length of their longest common subsequence.

The implementation uses a dynamic programming approach to compute the length of the LCS. It creates a 2D slice `dp` of size `(m+1) x (n+1)` where `m` and `n` are the lengths of `s1` and `s2`, respectively. The value `dp[i][j]` represents the length of the LCS of the first `i` characters of `s1` and the first `j` characters of `s2`.

The algorithm fills in the `dp` table row by row, starting from the first row and column. For each cell `dp[i][j]`, if the characters `s1[i-1]` and `s2[j-1]` are the same, then the LCS of the first `i` characters of `s1` and the first `j` characters of `s2` is equal to the LCS of the first `i-1` characters of `s1` and the first `j-1` characters of `s2`, plus one. Otherwise, the LCS is equal to the maximum of the LCS of the first `i-1` characters of `s1` and the first `j` characters of `s2`, and the LCS of the first `i` characters of `s1` and the first `j-1` characters of `s2`.

Finally, the function returns `dp[m][n]`, which represents the length of the LCS of the entire strings `s1` and `s2`.


Sure! Here's an implementation of the Longest Palindromic Subsequence (LPS) problem using dynamic programming in Go:


```golang
// Finds the length of the longest palindromic subsequence of a string using dynamic programming
func LongestPalindromicSubsequenceLength(s string) int {
 n := len(s)
 dp := make([][]int, n)
 for i := range dp {
 dp[i] = make([]int, n)
 dp[i][i] = 1
 }

 for l := 2; l <= n; l++ {
 for i := 0; i <= n-l; i++ {
 j := i + l - 1
 if s[i] == s[j] {
 dp[i][j] = dp[i+1][j-1] + 2
 } else {
 dp[i][j] = max(dp[i+1][j], dp[i][j-1])
 }
 }
 }

 return dp[0][n-1]
}

// Returns the maximum of two integers
func max(a, b int) int {
 if a > b {
 return a
 }
 return b
}
```
The `LongestPalindromicSubsequenceLength` function takes a string `s` as input and returns an integer representing the length of the longest palindromic subsequence in `s`.

The implementation uses a dynamic programming approach to compute the length of the LPS. It creates a 2D slice `dp` of size `n x n`, where `n` is the length of the input string `s`. The value `dp[i][j]` represents the length of the LPS of the substring `s[i...j]`.

The algorithm fills in the `dp` table diagonally, starting from the main diagonal. The base cases are when the length of the substring is 1, in which case `dp[i][i]` is always 1. For substrings of length 2 or greater, the algorithm iterates over all possible substrings of length `l`, starting from 2 and going up to `n`. For each substring `s[i...j]`, if `s[i]` and `s[j]` are the same, then the LPS of `s[i...j]` is equal to the LPS of `s[i+1...j-1]`, plus 2. Otherwise, the LPS of `s[i...j]` is equal to the maximum of the LPS of `s[i+1...j]` and the LPS of `s[i...j-1]`.

Finally, the function returns `dp[0][n-1]`, which represents the length of the LPS of the entire input string `s`.


Sure! Here's an implementation of the Longest Palindromic Substring (LPS) problem using dynamic programming in Go:


```golang
// Finds the longest palindromic substring of a string using dynamic programming
func LongestPalindromicSubstring(s string) string {
 n := len(s)
 dp := make([][]bool, n)
 for i := range dp {
 dp[i] = make([]bool, n)
 }

 start, maxLength := 0, 1

 // All substrings of length 1 are palindromes
 for i := 0; i < n; i++ {
 dp[i][i] = true
 }

 // Check for substrings of length 2
 for i := 0; i < n-1; i++ {
 if s[i] == s[i+1] {
 dp[i][i+1] = true
 start = i
 maxLength = 2
 }
 }

 // Check for substrings of length 3 or more
 for k := 3; k <= n; k++ {
 for i := 0; i < n-k+1; i++ {
 j := i + k - 1
 if dp[i+1][j-1] && s[i] == s[j] {
 dp[i][j] = true
 if k > maxLength {
 start = i
 maxLength = k
 }
 }
 }
 }

 return s[start : start+maxLength]
}
```
The `LongestPalindromicSubstring` function takes a string `s` as input and returns a string representing the longest palindromic substring in `s`.

The implementation uses a dynamic programming approach to find the LPS. It creates a 2D slice `dp` of size `n x n`, where `n` is the length of the input string `s`. The value `dp[i][j]` is true if the substring `s[i...j]` is a palindrome, and false otherwise.

The algorithm first initializes all substrings of length 1 as palindromes, and then checks for palindromes of length 2. For substrings of length 3 or more, the algorithm checks if the substring `s[i+1...j-1]` is a palindrome and if `s[i]` is equal to `s[j]`. If so, the substring `s[i...j]` is also a palindrome.

The algorithm keeps track of the starting index and length of the longest palindromic substring seen so far, and returns this substring at the end of the function.

Finally, the function returns the substring `s[start : start+maxLength]`, which represents the longest palindromic substring in the input string `s`.


Certainly! Here's an implementation of the Edit Distance problem using dynamic programming in Go:


```golang
// Computes the minimum edit distance between two strings using dynamic programming
func EditDistance(s1, s2 string) int {
 m, n := len(s1), len(s2)
 dp := make([][]int, m+1)
 for i := range dp {
 dp[i] = make([]int, n+1)
 }

 // Base cases
 for i := 0; i <= m; i++ {
 dp[i][0] = i
 }
 for j := 0; j <= n; j++ {
 dp[0][j] = j
 }

 // Compute edit distance for substrings of s1 and s2
 for i := 1; i <= m; i++ {
 for j := 1; j <= n; j++ {
 if s1[i-1] == s2[j-1] {
 dp[i][j] = dp[i-1][j-1]
 } else {
 dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
 }
 }
 }

 return dp[m][n]
}

// Helper function to compute the minimum of three integers
func min(a, b, c int) int {
 if a < b {
 if a < c {
 return a
 } else {
 return c
 }
 } else {
 if b < c {
 return b
 } else {
 return c
 }
 }
}
```
The `EditDistance` function takes two strings `s1` and `s2` as input and returns an integer representing the minimum edit distance between `s1` and `s2`.

The implementation uses a dynamic programming approach to compute the edit distance. It creates a 2D slice `dp` of size `(m+1) x (n+1)`, where `m` and `n` are the lengths of `s1` and `s2`, respectively. The value `dp[i][j]` represents the minimum edit distance between the substrings `s1[0...i-1]` and `s2[0...j-1]`.

The algorithm initializes the base cases: if one of the strings is empty, the edit distance is the length of the other string. It then computes the edit distance for substrings of `s1` and `s2` using the following recurrence relation:

* If the characters at `s1[i-1]` and `s2[j-1]` are the same, then the edit distance is the same as the edit distance between the substrings `s1[0...i-2]` and `s2[0...j-2]`.
* Otherwise, the edit distance is 1 plus the minimum of the edit distance between `s1[0...i-1]` and `s2[0...j-2]` (deletion), `s1[0...i-2]` and `s2[0...j-1]` (insertion), and `s1[0...i-2]` and `s2[0...j-2]` (substitution).

The algorithm returns the value `dp[m][n]`, which represents the minimum edit distance between the input strings `s1` and `s2`.

In addition, the implementation includes a helper function `min` that computes the minimum of three integers.


Sure! Here's an implementation of the Z algorithm for pattern searching in Golang:


```golang
package main

import "fmt"

func calculateZArray(str string) []int {
 length := len(str)
 zArray := make([]int, length)
 zArray[0] = length
 
 left, right := 0, 0
 for i := 1; i < length; i++ {
 if i > right {
 left, right = i, i
 for right < length && str[right] == str[right-left] {
 right++
 }
 zArray[i] = right - left
 right--
 } else {
 k := i - left
 if zArray[k] < right-i+1 {
 zArray[i] = zArray[k]
 } else {
 left = i
 for right < length && str[right] == str[right-left] {
 right++
 }
 zArray[i] = right - left
 right--
 }
 }
 }
 
 return zArray
}

func searchPattern(pattern, text string) []int {
 str := pattern + "$" + text
 length := len(str)
 zArray := calculateZArray(str)
 
 var result []int
 for i := 0; i < length; i++ {
 if zArray[i] == len(pattern) {
 result = append(result, i-len(pattern)-1)
 }
 }
 
 return result
}

func main() {
 text := "ABXABCABZABXABYABXABCABY"
 pattern := "AB"
 result := searchPattern(pattern, text)
 fmt.Println(result)
}
```
In this implementation, `calculateZArray` function calculates the Z array for a given string. The `searchPattern` function appends the positions of pattern occurrences to a result slice and returns it. The main function demonstrates how to use the `searchPattern` function.


# Chapter 11: Tree Algorithms
Sure! Here's an implementation of a binary search tree in Golang that includes pre-order, in-order, and post-order traversal methods:


```golang
package main

import "fmt"

type Node struct {
 Value int
 Left *Node
 Right *Node
}

type BinarySearchTree struct {
 Root *Node
}

func (bst \*BinarySearchTree) Insert(value int) {
 newNode := &Node{Value: value}
 if bst.Root == nil {
 bst.Root = newNode
 } else {
 current := bst.Root
 for {
 if value < current.Value {
 if current.Left == nil {
 current.Left = newNode
 break
 } else {
 current = current.Left
 }
 } else {
 if current.Right == nil {
 current.Right = newNode
 break
 } else {
 current = current.Right
 }
 }
 }
 }
}

func (bst \*BinarySearchTree) PreOrderTraversal(node *Node) {
 if node == nil {
 return
 }
 fmt.Printf("%d ", node.Value)
 bst.PreOrderTraversal(node.Left)
 bst.PreOrderTraversal(node.Right)
}

func (bst \*BinarySearchTree) InOrderTraversal(node *Node) {
 if node == nil {
 return
 }
 bst.InOrderTraversal(node.Left)
 fmt.Printf("%d ", node.Value)
 bst.InOrderTraversal(node.Right)
}

func (bst \*BinarySearchTree) PostOrderTraversal(node *Node) {
 if node == nil {
 return
 }
 bst.PostOrderTraversal(node.Left)
 bst.PostOrderTraversal(node.Right)
 fmt.Printf("%d ", node.Value)
}

func main() {
 bst := &BinarySearchTree{}
 bst.Insert(50)
 bst.Insert(30)
 bst.Insert(70)
 bst.Insert(20)
 bst.Insert(40)
 bst.Insert(60)
 bst.Insert(80)
 fmt.Println("Pre-order traversal:")
 bst.PreOrderTraversal(bst.Root)
 fmt.Println("\nIn-order traversal:")
 bst.InOrderTraversal(bst.Root)
 fmt.Println("\nPost-order traversal:")
 bst.PostOrderTraversal(bst.Root)
}
```
In this implementation, `Node` represents a single node in the binary search tree, and `BinarySearchTree` represents the tree itself. The `Insert` method adds a new node to the tree at the appropriate location according to its value.

The `PreOrderTraversal`, `InOrderTraversal`, and `PostOrderTraversal` methods perform the respective traversals on the tree, starting from the given node. In the `main` function, we create a binary search tree, insert some values into it, and then print out the results of the three different traversal methods.


Sure! Here's an implementation of an AVL tree in Golang that demonstrates its self-balancing properties by inserting and deleting nodes:


```golang
package main

import "fmt"

type Node struct {
 Value int
 Height int
 Left *Node
 Right *Node
}

type AVLTree struct {
 Root *Node
}

func (tree \*AVLTree) Insert(value int) {
 newNode := &Node{Value: value, Height: 1}
 if tree.Root == nil {
 tree.Root = newNode
 return
 }
 tree.Root = tree.Root.insert(newNode)
}

func (node \*Node) insert(newNode *Node) *Node {
 if newNode.Value < node.Value {
 if node.Left == nil {
 node.Left = newNode
 } else {
 node.Left = node.Left.insert(newNode)
 }
 } else {
 if node.Right == nil {
 node.Right = newNode
 } else {
 node.Right = node.Right.insert(newNode)
 }
 }
 node = node.balance()
 return node
}

func (node \*Node) balance() *Node {
 leftHeight := node.height(node.Left)
 rightHeight := node.height(node.Right)
 if leftHeight-rightHeight > 1 {
 if node.Left.balanceFactor() < 0 {
 node.Left = node.Left.rotateLeft()
 }
 node = node.rotateRight()
 } else if rightHeight-leftHeight > 1 {
 if node.Right.balanceFactor() > 0 {
 node.Right = node.Right.rotateRight()
 }
 node = node.rotateLeft()
 }
 node.Height = 1 + node.heightMax(node.Left, node.Right)
 return node
}

func (node \*Node) rotateRight() *Node {
 newRoot := node.Left
 node.Left = newRoot.Right
 newRoot.Right = node
 node.Height = 1 + node.heightMax(node.Left, node.Right)
 newRoot.Height = 1 + node.heightMax(newRoot.Left, newRoot.Right)
 return newRoot
}

func (node \*Node) rotateLeft() *Node {
 newRoot := node.Right
 node.Right = newRoot.Left
 newRoot.Left = node
 node.Height = 1 + node.heightMax(node.Left, node.Right)
 newRoot.Height = 1 + node.heightMax(newRoot.Left, newRoot.Right)
 return newRoot
}

func (node \*Node) height(n *Node) int {
 if n == nil {
 return 0
 }
 return n.Height
}

func (node \*Node) heightMax(left, right *Node) int {
 if node.height(left) > node.height(right) {
 return node.height(left)
 }
 return node.height(right)
}

func (node \*Node) balanceFactor() int {
 return node.height(node.Left) - node.height(node.Right)
}

func (tree \*AVLTree) Delete(value int) {
 if tree.Root == nil {
 return
 }
 tree.Root = tree.Root.delete(value)
}

func (node \*Node) delete(value int) *Node {
 if value < node.Value {
 node.Left = node.Left.delete(value)
 } else if value > node.Value {
 node.Right = node.Right.delete(value)
 } else {
 if node.Left == nil {
 return node.Right
 } else if node.Right == nil {
 return node.Left
 } else {
 minNode := node.Right.min()
 node.Value = minNode.Value
 node.Right = node.Right.delete(minNode.Value)
 }
 }
 node = node.balance()
 return node
```

