---
tags: ['go']
title: File Handling and Error Handling in Go.
description: File Handling and Error Handling in Go.
pubDate: Fri, 21 October 2024
layout: "@/templates/BasePost.astro"
imgSrc: /imgs/2023/2898315273.png
---
Sure, let's talk about file handling and error handling in Go.

File Handling in Go
-------------------

Go provides a rich set of functions and libraries for working with files. The `os` package provides a set of functions for working with the file system, including creating, opening, reading, and writing files.

Here's an example of how to read the contents of a file in Go:


```go
package main

import (
 "fmt"
 "io/ioutil"
)

func main() {
 data, err := ioutil.ReadFile("example.txt")
 if err != nil {
 fmt.Println("Error reading file:", err)
 return
 }

 fmt.Println("File contents:", string(data))
}
```
In this code, we use the `ioutil.ReadFile` function to read the contents of a file named `example.txt`. This function returns a byte slice containing the contents of the file, as well as an error value. If an error occurs while reading the file, we print an error message and return from the function.

We then print the contents of the file to the console using the `fmt.Println` function.

Error Handling in Go
--------------------

Go places a strong emphasis on error handling, and provides a number of features to help you handle errors in your code.

One of the most common ways to handle errors in Go is to return an error value from a function. An error value is simply a value that implements the `error` interface, which has a single method, `Error() string`, that returns a string describing the error.

Here's an example of how to return an error value from a function:


```go
package main

import "errors"

func divide(a, b float64) (float64, error) {
 if b == 0 {
 return 0, errors.New("division by zero")
 }

 return a / b, nil
}

func main() {
 result, err := divide(10, 0)
 if err != nil {
 println("Error:", err.Error())
 return
 }

 println("Result:", result)
}
```
In this code, we define a function called `divide` that takes two float64 values and returns their quotient, as well as an error value if the second argument is zero. We use the `errors.New` function to create a new error value with a custom error message.

In the `main` function, we call the `divide` function with a zero value for the second argument, causing an error to occur. We then check if the error value is not nil, and print an error message if it is.

By returning error values from functions and checking for errors in the calling code, you can ensure that your code handles errors gracefully and provides informative error messages to users.


Sure, let's dive into reading and writing files in Go.

Reading Files in Go
-------------------

Go provides several ways to read the contents of a file. One common way is to use the `os` package, which provides functions for working with the operating system. Specifically, we can use the `os.Open` and `os.Read` functions to open a file and read its contents, respectively.


```go
package main

import (
 "fmt"
 "os"
)

func main() {
 file, err := os.Open("example.txt")
 if err != nil {
 fmt.Println(err)
 return
 }
 defer file.Close()

 buf := make([]byte, 1024)
 for {
 n, err := file.Read(buf)
 if n == 0 {
 break
 }
 if err != nil {
 fmt.Println(err)
 return
 }
 fmt.Print(string(buf[:n]))
 }
}
```
In this example, we first use `os.Open` to open the file `example.txt`. If an error occurs, we print it and return from the function. We defer closing the file to ensure it is closed when we are finished with it.

Next, we read the file contents in a loop using `file.Read`, which reads up to len(buf) bytes from the file into the buffer `buf`. We print the contents of the buffer using `fmt.Print` and continue reading until the end of the file is reached.

Writing Files in Go
-------------------

Similarly to reading files, Go provides several ways to write data to a file. One common way is to use the `os` package again, this time with the `os.Create` and `os.Write` functions.


```go
package main

import (
 "fmt"
 "os"
)

func main() {
 file, err := os.Create("example.txt")
 if err != nil {
 fmt.Println(err)
 return
 }
 defer file.Close()

 data := []byte("hello world\n")
 _, err = file.Write(data)
 if err != nil {
 fmt.Println(err)
 return
 }
}
```
In this example, we use `os.Create` to create a new file named `example.txt`. If an error occurs, we print it and return from the function. We defer closing the file to ensure it is closed when we are finished with it.

Next, we write the data `hello world\n` to the file using `file.Write`. The number of bytes written is returned, but we ignore it in this example.

By using these simple functions, you can easily read from and write to files in Go. Remember to always handle errors appropriately to ensure your code is robust and reliable.


In Go, error handling is an important aspect of writing robust and reliable code. Go has a built-in error type, `error`, which is used to represent errors in the language. The `error` type is an interface with a single method, `Error() string`, that returns a string describing the error.

In Go, it is common to return errors as a second return value from functions. This allows the caller to check for errors and take appropriate action. For example, the `os.Open` function returns a `*os.File` and an `error`:


```go
func Open(name string) (*File, error)
```
If the file can be opened successfully, `Open` returns a valid `*os.File` and `nil` error. If there is an error, `Open` returns a `nil` `*os.File` and a non-`nil` error.

Here is an example of error handling in Go:


```go
package main

import (
 "fmt"
 "os"
)

func main() {
 file, err := os.Open("example.txt")
 if err != nil {
 fmt.Println("error opening file:", err)
 return
 }
 defer file.Close()

 // Read file contents...
}
```
In this example, we use `os.Open` to open a file named `example.txt`. If an error occurs, `Open` returns a non-`nil` error, and we print an error message and return from the function.

It's important to handle errors in this way to ensure that your code is robust and reliable. By returning errors as a second return value and checking for them using `if err != nil`, you can easily detect and handle errors in your Go code.

In addition to returning errors, Go also has a built-in `panic` function that can be used to terminate a program if an unrecoverable error occurs. However, using `panic` should be avoided in most cases, and errors should be returned instead.



In bash, you can move files using the `mv` command. Here's an example of how you could use `mv` in a script:


```bash
#!/bin/bash

# Define the source and destination directories
src_dir="/path/to/source/directory"
dst_dir="/path/to/destination/directory"

# Use the `mv` command to move all files from the source directory to the destination directory
for file in "$src\_dir"/*; do
 mv "$file" "$dst\_dir"
done
```
This script moves all files in the `src_dir` to the `dst_dir`. The `for` loop iterates through all files in `src_dir` and uses the `mv` command to move each file to the `dst_dir`.

Note: This script will overwrite any existing files in the `dst_dir` with the same names as the files being moved. If you want to avoid overwriting existing files, you can modify the script to include a check for file existence in the destination directory before moving the file.


Here's an example of how you could write a Go program to move files:


```go
package main

import (
 "fmt"
 "os"
 "path/filepath"
)

func main() {
 srcDir := "/path/to/source/directory"
 dstDir := "/path/to/destination/directory"

 err := filepath.Walk(srcDir, func(path string, info os.FileInfo, err error) error {
 if info.IsDir() {
 return nil
 }

 relPath, _ := filepath.Rel(srcDir, path)
 dstPath := filepath.Join(dstDir, relPath)

 fmt.Printf("Moving file from %s to %s\n", path, dstPath)

 return os.Rename(path, dstPath)
 })

 if err != nil {
 fmt.Printf("An error occurred while moving files: %s\n", err)
 return
 }

 fmt.Println("Files successfully moved.")
}
```
This program uses the `filepath.Walk` function to iterate through all the files in the `srcDir` directory. For each file, it uses `filepath.Rel` to get the relative path of the file with respect to `srcDir`, and then uses `filepath.Join` to construct the destination path by joining the relative path with the `dstDir` directory. Finally, it uses the `os.Rename` function to move the file to the destination directory.

Note: This program will overwrite any existing files in the `dstDir` with the same names as the files being moved. If you want to avoid overwriting existing files, you can modify the program to include a check for file existence in the destination directory before moving the file.


```go 
 package main

import (
	"fmt"
	"html/template"
	"io"
	"os"
	"path/filepath"
	"strings"

	"github.com/bitfield/script"
)

// basic go cli tool
func main() {
	// go through each directory in go using os package
	htmlFiles := []string{}
	outputFolder := "gh-pages"
	reg := []string{"rm", "-rf", outputFolder}
	cmd := strings.Join(reg[:], " ")

	tmpl := `
	<html>
		<head>
			<title>List of Matlab Reports and Files</title>
		</head>
		<body>
			<h1>List of Files</h1>
			<ul>
			{{ range . }}
				<li><a href={{.}}>{{ . }}</a></li>
			{{ end }}
			</ul>
		</body>
	</html>
	` 
 ```

It looks like you're starting to write a Go program to generate an HTML file that lists all of the files in a directory, and move the generated HTML file to an `outputFolder`. Here's an example of how you could complete this program:


```go
package main

import (
 "fmt"
 "html/template"
 "io/ioutil"
 "os"
 "path/filepath"
 "strings"
)

func main() {
 htmlFiles := []string{}
 outputFolder := "gh-pages"
 srcDir := "."

 err := filepath.Walk(srcDir, func(path string, info os.FileInfo, err error) error {
 if !info.IsDir() {
    htmlFiles = append(htmlFiles, path)
 }
  return nil
 })

 if err != nil {
  fmt.Printf("An error occurred while reading files: %s\n", err)
  return
 }

 tmpl := template.Must(template.New("index").Parse(`
 <html>
  <head>
  <title>List of Files</title>
  </head>
  <body>
  <h1>List of Files</h1>
  <ul>
  {{ range . }}
  <li><a href={{.}}>{{ . }}</a></li>
  {{ end }}
  </ul>
  </body>
  </html>
 `))

 f, err := os.Create("index.html")
 if err != nil {
  fmt.Printf("An error occurred while creating index.html: %s\n", err)
  return
 }
 defer f.Close()

 if err := tmpl.Execute(f, htmlFiles); err != nil {
  fmt.Printf("An error occurred while executing the template: %s\n", err)
  return
 }

 err = os.MkdirAll(outputFolder, os.ModePerm)
 if err != nil {
  fmt.Printf("An error occurred while creating the output folder: %s\n", err)
  return
 }

 src, err := os.Open("index.html")
 if err != nil {
  fmt.Printf("An error occurred while opening index.html: %s\n", err)
  return
 }
 defer src.Close()

 dst, err := os.Create(filepath.Join(outputFolder, "index.html"))
 if err != nil {
  fmt.Printf("An error occurred while creating the output file: %s\n", err)
  return
 }
 defer dst.Close()

 _, err = io.Copy(dst, src)
 if err != nil {
  fmt.Printf("An error occurred while copying index.html: %s\n", err)
  return
 }

 fmt.Println("Files successfully moved.")
}
```
This program


```go 
 	script.FindFiles(".").FilterScan(func(line string, w io.Writer) {
		// if line contains html print it
		if strings.Contains(line, ".html") || strings.Contains(line, ".pdf") {
			fmt.Fprintf(w, "scanned line: %q\n", line)
			htmlFiles = append(htmlFiles, line)
		}
	}).Stdout()

	fmt.Println(htmlFiles)
	// create html directory
	script.Exec("mkdir " + outputFolder).Stdout()

	// for each html file
	for _, file := range htmlFiles {
		reg = []string{"cp", file, outputFolder}
		cmd = strings.Join(reg[:], " ")
		// copy file to html directory
		script.Exec(cmd).Stdout()
	}

	// move ads.txt to html directory
	script.Exec("mv ads.txt " + outputFolder).Stdout()
 
 ```

The code you posted implements a basic Go CLI tool that moves HTML and PDF files to a new directory named "gh-pages". Here's a brief explanation of the code:

* First, the code uses the FindFiles function from the `github.com/bitfield/script` package to scan the current directory for files that contain ".html" or ".pdf" in their name. The matching files are then stored in the `htmlFiles` slice.
* Next, the code uses the `script.Exec` function to create the "gh-pages" directory using the `mkdir` command.
* The code then iterates over the `htmlFiles` slice and uses `script.Exec` to copy each file to the "gh-pages" directory using the `cp` command.
* Finally, the code uses `script.Exec` to move the "ads.txt" file to the "gh-pages" directory using the `mv` command.

Note that this code only implements the file moving part of the deployment to Github Pages, you might need to write additional code to deploy the files to Github Pages.


```go 
 	if err != nil {
		fmt.Println(err)
		return
	}

	file, err := os.Create(outputFolder + "/index.html")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer file.Close()
	// remove outputFolder from htmlFiles
	for i, file := range htmlFiles {
		// get basename of file
		baseName := filepath.Base(file)
		htmlFiles[i] = baseName
	}
	err = t.Execute(file, htmlFiles)
	if err != nil {
		fmt.Println(err)
		return
	} 
 ```

The code you posted creates an HTML file named "index.html" in the "gh-pages" directory and writes the list of files in the `htmlFiles` slice to the HTML file. Here's a brief explanation of the code:

* First, the code creates a file in the "gh-pages" directory using the `os.Create` function.
* The code then iterates over the `htmlFiles` slice and retrieves the base name of each file using the `filepath.Base` function. The base name is stored back in the `htmlFiles` slice.
* Finally, the code uses the `t.Execute` function to write the `htmlFiles` slice to the "index.html" file. The `t.Execute` function uses the template defined in the `tmpl` variable to format the HTML output.

Note that the code also contains error handling to check for any errors that might occur during the file creation and writing process. If an error occurs, the code prints the error message and returns from the main function.


```yaml
 # run go main.go and install and then deploy to gh-pages
name: deploy

on:
  push:
    branches: [master]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Set up Go
        uses: actions/setup-go@v2
        with:
          go-version: 1.19

      - name: Build
        run: |
          go build -o main .
          ./main
          echo google.com, pub-2479144310234386, DIRECT, f08c47fec0942fa0 > ads.txt
          mv ads.txt ./gh-pages

      - name: Deploy to gh-pages
        uses:
          peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./gh-pages
 
 ```

The code you posted is a GitHub Actions workflow that builds and deploys a Go program to GitHub Pages. Here's a brief explanation of the code:

* The workflow is triggered when a push is made to the "master" branch.
* The first step checks out the code from the repository.
* The second step sets up Go using the actions/setup-go@v2 action.
* The third step builds the Go program using the "go build" command, runs the program using "./main", and then adds an "ads.txt" file to the "gh-pages" directory.
* The fourth step deploys the contents of the "gh-pages" directory to GitHub Pages using the peaceiris/actions-gh-pages@v3 action. The action requires the GitHub token to be passed as an input parameter.

Note that the workflow uses the latest version of Ubuntu for the build environment and that the "gh-pages" directory contains the generated HTML file and other files that will be deployed to GitHub Pages.


### References
- https://raw.githubusercontent.com/FriendlyUser/Matlab/master/.github/workflows/deploy.yml
- https://raw.githubusercontent.com/FriendlyUser/Matlab/master/main.go
