---
tags: ['go']
title:  Concurrency in Go .
description: Concurrency in Go.
pubDate: Fri, 21 October 2024
layout: "@/templates/BasePost.astro"
imgSrc: /imgs/2023/241285989.png
---
Concurrency is a powerful feature of Go programming language. With its simple syntax and efficient design, Go provides an easy-to-use and high-performance environment for building concurrent programs. In this post, we'll explore the basics of concurrency in Go and learn how to write concurrent programs using goroutines and channels.

### Goroutines

Goroutines are the building blocks of concurrent programs in Go. A goroutine is a lightweight thread of execution that can be started with the ` keyword. Goroutines are multiplexed onto a smaller set of operating system threads by the Go runtime, which allows many goroutines to run simultaneously on a single CPU.

Here's an example of how to start a goroutine:


```go
func sayHello() {
 fmt.Println("Hello, world!")
}

func main() {
 go sayHello()
 // do other things
}
```
In this example, we define a function called `sayHello` that prints "Hello, world!" to the console. We then use the ` keyword to start a goroutine that executes this function. Note that the ` keyword does not block the main goroutine, which allows us to do other things while the `sayHello` goroutine is running.

### Channels

Channels are another important feature of concurrency in Go. A channel is a typed conduit through which you can send and receive values with the channel operator, `<-`. Channels allow you to synchronize the execution of concurrent goroutines and communicate between them.

Here's an example of how to create and use a channel:


```go
func writeToChannel(ch chan<- string) {
 ch <- "Hello, world!"
}

func main() {
 ch := make(chan string)
 go writeToChannel(ch)
 msg := <-ch
 fmt.Println(msg)
}
```
In this example, we define a function called `writeToChannel` that takes a channel of strings as an argument and sends the string "Hello, world!" through the channel using the channel operator, `<-`. We then create a channel of strings using the `make` function, start a goroutine that calls the `writeToChannel` function with this channel, and finally receive the message sent through the channel using the channel operator, `<-`.

### Conclusion

Concurrency is an important feature of modern programming languages, and Go provides a simple and efficient way to write concurrent programs using goroutines and channels. By using these building blocks, you can create high-performance and scalable programs that take full advantage of modern hardware.


Goroutines are the building blocks of concurrent programs in Go. They are lightweight threads of execution that can be started with the ` keyword. Goroutines are managed by the Go runtime, which multiplexes them onto a smaller set of operating system threads, allowing many goroutines to run simultaneously on a single CPU.

One of the key benefits of goroutines is that they make it easy to write concurrent programs in Go. By using goroutines, you can perform multiple tasks simultaneously without having to deal with the complexities of thread management or locking. Goroutines are also very efficient, as they have a small memory footprint and can be created and destroyed quickly.

To start a goroutine, you simply need to define a function that you want to run concurrently and prefix it with the ` keyword. For example, the following code starts a goroutine that runs the `sayHello` function:


```go
func sayHello() {
 fmt.Println("Hello, world!")
}

func main() {
 go sayHello()
 // do other things
}
```
When you run this code, the `sayHello` function will execute concurrently with the `main` function, allowing you to perform other tasks while the `sayHello` function is running.

Goroutines can also be used to perform more complex concurrent tasks, such as reading from and writing to channels. By combining goroutines and channels, you can create powerful concurrent programs that are both efficient and easy to reason about.


Channels are a powerful feature of Go that enable you to send and receive data between goroutines. A channel is a typed conduit that can be used to communicate between goroutines, allowing them to synchronize their execution and exchange information.

To create a channel, you use the `make` function and specify the type of data that the channel will carry. For example, the following code creates a channel of strings:


```go
ch := make(chan string)
```
Once you have a channel, you can use the `<-` operator to send and receive data. The `<-` operator can be used in two ways: to send data through a channel or to receive data from a channel.

To send data through a channel, you use the `<-` operator on the channel, followed by the data that you want to send. For example:


```go
ch <- "Hello, world!"
```
This code sends the string "Hello, world!" through the `ch` channel.

To receive data from a channel, you use the `<-` operator on the left side of the channel variable. For example:


```go
msg := <-ch
```
This code receives a string from the `ch` channel and assigns it to the `msg` variable.

Channels can be used in many different ways, depending on your needs. For example, you can use channels to synchronize the execution of multiple goroutines, to implement a producer-consumer pattern, or to perform load balancing across multiple workers.

One of the key benefits of channels is that they provide a simple and efficient way to write concurrent programs in Go. By using channels to coordinate the execution of goroutines, you can create programs that are both easy to reason about and scalable.


The select statement is a powerful feature of Go that allows you to wait on multiple channels at once. It is often used in concurrent programs to synchronize the execution of multiple goroutines.

The select statement is similar to a switch statement, but instead of switching on values, it switches on channels. The select statement waits until one of the channels is ready to send or receive data, and then executes the corresponding case statement.

Here's an example of how the select statement works:


```go
ch1 := make(chan string)
ch2 := make(chan string)

go func() {
 time.Sleep(time.Second)
 ch1 <- "Hello"
}()

go func() {
 time.Sleep(time.Second)
 ch2 <- "World"
}()

select {
case msg1 := <-ch1:
 fmt.Println(msg1)
case msg2 := <-ch2:
 fmt.Println(msg2)
}
```
In this code, we create two channels `ch1` and `ch2`, and then start two goroutines that send data through the channels after a one second delay. We then use the select statement to wait for data from either channel, and print the message that is received.

The select statement is powerful because it allows you to wait on multiple channels at once, and respond to the first one that is ready. This can be useful in situations where you want to wait for input from multiple sources, such as user input or network requests.

It's worth noting that the select statement can also include a default case, which is executed if none of the channels are ready to send or receive data. This can be useful for situations where you want to perform some action if no input is received after a certain period of time, for example.


Sure! Here's a simple CLI app that demonstrates the use of goroutines and channels in Go. This app simulates a server that receives requests and processes them concurrently using goroutines. The requests are sent to the server via a channel, and the responses are returned via another channel.


```go
package main

import (
 "fmt"
 "time"
)

type Request struct {
 ID int
 Message string
}

type Response struct {
 ID int
 Message string
}

func server(requests <-chan \*Request, responses chan<- \*Response) {
 for {
 req := <-requests

 // Process request concurrently
 go func(req \*Request) {
 time.Sleep(time.Second)
 responses <- &Response{
 ID: req.ID,
 Message: fmt.Sprintf("Processed request %d: %s", req.ID, req.Message),
 }
 }(req)
 }
}

func main() {
 requests := make(chan *Request)
 responses := make(chan *Response)

 // Start server
 go server(requests, responses)

 // Send requests to server
 for i := 1; i <= 5; i++ {
 req := &Request{
 ID: i,
 Message: fmt.Sprintf("Hello %d", i),
 }
 requests <- req
 }

 // Receive responses from server
 for i := 1; i <= 5; i++ {
 res := <-responses
 fmt.Println(res.Message)
 }
}
```
In this code, we define two types, `Request` and `Response`, which represent the requests and responses that the server will process. We then define the `server` function, which takes two channels as arguments: `requests`, which is used to receive requests, and `responses`, which is used to send responses.

The `server` function runs in an infinite loop, waiting for requests to arrive on the `requests` channel. When a request arrives, it processes it concurrently using a goroutine, and then sends the response back through the `responses` channel.

In the `main` function, we create two channels, `requests` and `responses`, and start the server by calling the `server` function with these channels as arguments. We then send five requests to the server, and wait for the responses to arrive, printing them to the console when they do.

When you run this code, you should see the following output:


```go
yaml`Processed request 1: Hello 1
Processed request 2: Hello 2
Processed request 3: Hello 3
Processed request 4: Hello 4
Processed request 5: Hello 5
```
This output shows that the requests were processed concurrently, as they were received and printed out in a random order. This demonstrates the power of goroutines and channels in Go, and how they can be used to write efficient and scalable concurrent programs.


### Parsing comments from reddit

Reddit is a social news aggregation, web content rating, and discussion website. Users can submit posts, such as text or direct links, and other users can vote on these posts, causing them to rise or fall in popularity. Reddit is organized into communities, known as "subreddits," which cover a vast array of topics and interests.


Web scraping with Go (Golang) can be useful in a variety of ways:

1. Data collection: Web scraping allows you to extract large amounts of data from websites, which can be useful for data analysis and research.
2. Price monitoring: Go can be used to monitor the prices of products on various websites and notify users of price changes.
3. Content aggregation: Go can be used to aggregate content from multiple websites into a single source, making it easier to find and view relevant information.
4. Automation: Go can be used to automate repetitive tasks, such as filling out forms or visiting websites, to save time and effort.
5. Testing: Go can be used to test websites for functional and performance issues, making it easier to identify and fix problems.

In summary, web scraping with Go is useful for data collection, price monitoring, content aggregation, automation, and testing, among other uses.


Parsing subreddits with the Reddit API involves using the API to extract data from Reddit and display it in a specific format. To parse subreddits using the Reddit API, you need to have an API key or access token. Once you have this, you can make HTTP requests to the Reddit API to retrieve data for a specific subreddit. The API will return the data in JSON format, which can then be processed and displayed in a way that meets your needs.

For example, to retrieve the top 10 posts in a subreddit, you can make a GET request to the following URL:

[https://www.reddit.com/r/[subreddit]/top.json?limit=10](https://www.reddit.com/r/%5Bsubreddit%5D/top.json?limit=10)

Where [subreddit] is the name of the subreddit you want to retrieve data from.

There are many libraries available in Go that simplify the process of making API calls and processing the resulting data. By using one of these libraries, you can focus on the data you want to extract and display, without having to worry about the details of making API calls and processing the results.


```go 
 package login 

import (
	"github.com/jzelinskie/geddit"
	"log"
	"github.com/dli-invest/finreddit/pkg/util"
)

// returns oauth session for reddit
// or fails - fine for my purposes
func RedditOAuth() (*geddit.OAuthSession, error) {
	client_id := util.GetEnvVar("REDDIT_CLIENT_ID")
	client_secret := util.GetEnvVar("REDDIT_CLIENT_SECRET")
	password := util.GetEnvVar("REDDIT_PASSWORD")
	username := util.GetEnvVar("REDDIT_USERNAME")
	o, err := geddit.NewOAuthSession(
		client_id,
		client_secret,
		"Stonk Market Scrapper see source https://github.com/dli-invest/finreddit",
		"http://friendlyuser.github.io",
	)
	if err != nil {
		log.Println(err)
		return nil, err
	}

	// Create new auth token for confidential clients (personal scripts/apps).
	err = o.LoginAuth(username, password)
	if err != nil {
		log.Println(err)
		return nil, err
	}
	return o, nil
} 
 ```

This code defines a Go function named "RedditOAuth" that is used to authenticate a user to the Reddit API using the "geddit" library. The function starts by retrieving four environment variables ("REDDIT\_CLIENT\_ID", "REDDIT\_CLIENT\_SECRET", "REDDIT\_PASSWORD", and "REDDIT\_USERNAME") using the "util.GetEnvVar" function from the "github.com/dli-invest/finreddit/pkg/util" package.

Next, the function creates a new OAuth session using the "geddit.NewOAuthSession" function and the retrieved environment variables. If an error occurs while creating the OAuth session, it is logged and returned.

Finally, the function logs in the user using the "o.LoginAuth" method and the "username" and "password" environment variables. If an error occurs while logging in, it is logged and returned. If the login is successful, the OAuth session is returned.


```go 
 package reddit

import (
	"fmt"
	"log"
	"strings"
	"time"

	"github.com/dli-invest/finreddit/pkg/csvs"
	"github.com/dli-invest/finreddit/pkg/discord"
	"github.com/dli-invest/finreddit/pkg/login"
	"github.com/dli-invest/finreddit/pkg/types"
	"github.com/dli-invest/finreddit/pkg/util"
	"github.com/jzelinskie/geddit"
)

// gets submissions a given SRConfiguration
func GetSubmissions(session *geddit.OAuthSession, cfg types.SRConfig) []*geddit.Submission {
	subreddit := cfg.Name
	limit := cfg.Limit
	subOpts := geddit.ListingOptions{
		Limit: limit,
	}
	if cfg.After != "" {
		subOpts.After = cfg.After
	}
	submissions, err := session.SubredditSubmissions(subreddit, geddit.NewSubmissions, subOpts)
	if err != nil {
		log.Fatal("Failed to retrieve subreddit posts for " + subreddit)
	}
	// further filter entries by minScore and minComments
	var validSubmissions = []*geddit.Submission{}

	for _, submission := range submissions {
		if submission.NumComments != 0 && cfg.MinScore != 0 {
			if submission.NumComments >= cfg.MinComments && submission.Score >= cfg.MinScore {
				validSubmissions = append(validSubmissions, submission)
				continue
			}
		}
		if cfg.LinkFlairText != "" {
			// checking for flair
			if strings.Contains(submission.LinkFlairText, cfg.LinkFlairText) {
				validSubmissions = append(validSubmissions, submission)
				continue
			}
		}
		if len(cfg.Phrases) != 0 {
			// search through phrases
			title := strings.ToLower(submission.Title)
			// check matches word
			for _, phrase := range cfg.Phrases {
				// check if phrase is contained in title
				lowerPhrase := strings.ToLower(phrase)
				addSubmission := strings.Contains(title, lowerPhrase)
				if addSubmission {
					validSubmissions = append(validSubmissions, submission)
					continue
				}
			}
		}
	}
	return validSubmissions
}

// Scans subreddits from config file
// for example cmd/scan_sr/simple.yml
func ScanSRs(cfgPathStr string) {
	// login to reddit
	o, err := login.RedditOAuth()
	if err != nil {
		log.Fatal("Failed to initialize Reddit Scrapper")
	}
	// read subreddits from config file
	cfgPath := util.MkPathFromStr(cfgPathStr)
	cfg, err := util.NewConfig(cfgPath)
	if err != nil {
		log.Fatal(err)
	}
	csvsPath := util.MkPathFromStr(cfg.Data.CsvPath)
	// print header row only used when
	if cfg.Data.NoMessage {
		fmt.Printf("%s\t%s\t%s\t%s\t%s\t%s\n", "subreddit", "url", "title", "author", "linkFlairText", "date")
	}
	for _, srCfg := range cfg.Data.SubReddits {
		srSubmissions := GetSubmissions(o, srCfg)
		for _, s := range srSubmissions {
			// check if submission is in csv already
			// aware that constantly opening the csv is inefficient
			// but I am dealing with a reasonable amount of entires
			hasValue := csvs.FindInCsv(csvsPath, s.FullID, 1)
			if hasValue {
				// no value, do nothing here
			} else {
				// seems like a lot of posts, wondering if I will hit
				// post limit, sleep 2 seconds after each post.
				// append to csv
				sData := [][]string{{srCfg.Name, s.FullID, s.URL}}
				csvs.AppendToCsv(csvsPath, sData)
				if cfg.Data.NoMessage {
					// output this as a csv for parsing in other programs
					// fmt.Println("Not sending to subreddit")
					fmt.Printf("%s\t%s\t%s\t%s\t%s\t%f\n", s.Subreddit, s.FullPermalink(), s.Title, s.Author, s.LinkFlairText, s.DateCreated)
				} else {
					discordPayload := MapSubmissionToEmbed(s)
					_, err := discord.SendWebhook(discordPayload)
					if err != nil {
						fmt.Println(s.FullID)
						fmt.Println(err)
					}
					time.Sleep(2 * time.Second)
				}
			}
		}
	}
}

func MapSubmissionToEmbed(submission *geddit.Submission) types.DiscordPayload {
	description := fmt.Sprintf(
		"%s (%d Likes, %d Comments)",
		submission.Author,
		submission.Score,
		submission.NumComments)
	// get timestamp
	var dateCreated int64 = int64(submission.DateCreated)
	t := time.Unix(dateCreated, 0)
	timestamp := t.Format(time.RFC3339)
	title := fmt.Sprintf("%s - %s", submission.Subreddit, submission.Title)
	discordEmbed := []types.DiscordEmbed{{
		Title:       title,
		Url:         submission.URL,
		Description: description,
		Timestamp:   timestamp,
	}}
	discordPayload := types.DiscordPayload{Embeds: discordEmbed}
	return discordPayload
}
 
 ```

This code is a Reddit scraper in Golang, which is a part of a project "finreddit". It uses the geddit library for connecting to the Reddit API and retrieve submissions from given subreddit. The code filters the submissions based on various conditions such as minimum score, minimum comments, link flair text, and certain phrases. The filtered submissions are then appended to a CSV file. The code also includes a ScanSRs function, which reads subreddit configurations from a YAML file, logs into Reddit using OAuth authentication, and retrieves the submissions using the GetSubmissions function.


```go 
 package csvs

// csv utilties to prevent duplicate entries
// probably manually clear out every now and then
import (
    "encoding/csv"
    "fmt"
    "os"
)

// read csv from file path
func ReadCsvFile(filePath string) [][]string {
    f, err := os.Open(filePath)
    if err != nil {
        fmt.Println("Unable to read input file " + filePath, err)
    }
    defer f.Close()

    csvReader := csv.NewReader(f)
    records, err := csvReader.ReadAll()
    if err != nil {
        fmt.Println("Unable to parse file as CSV for " + filePath, err)
    }

    return records
}

func AppendRowToCsv(fileName string, data []string) {
    f, err := os.OpenFile(fileName, os.O_WRONLY|os.O_CREATE|os.O_APPEND, 0644)
	if err != nil {
		fmt.Println(err)
		return
    }
    w := csv.NewWriter(f)
    err = w.Write(data)
    if err != nil {
        fmt.Println("Append Error")
        fmt.Println(err)
    }
    w.Flush()
}

// append rows to csvs
func AppendToCsv(fileName string, data [][]string) {
    f, err := os.OpenFile(fileName, os.O_WRONLY|os.O_CREATE|os.O_APPEND, 0644)
	if err != nil {
		fmt.Println(err)
		return
	}
    w := csv.NewWriter(f)
    for _, row:= range data {
        err = w.Write(row)
        if err != nil {
            fmt.Println("Append Error")
            fmt.Println(err)
        }
	}
	w.Flush()
}

// check if value exists in csv
func FindInCsv(filePath string, searchValue string, searchColumn int) (bool) {
    records := ReadCsvFile(filePath)
    foundValue := false
    for _, row:= range records {
        valueInRow := row[searchColumn]
        if searchValue == valueInRow {
            foundValue = true
            break
        }
	}
    return foundValue
} 
 ```

This is a Go library for working with CSV (Comma Separated Values) files. It provides functions to read, append and check if a value exists in a CSV file.

* `ReadCsvFile` reads a CSV file from the given file path and returns the data as a two-dimensional slice of strings.
* `AppendRowToCsv` appends a single row of data to the CSV file with the given file name.
* `AppendToCsv` appends multiple rows of data to the CSV file with the given file name.
* `FindInCsv` checks if a value exists in a specific column of the CSV file at the given file path. It returns a boolean indicating whether the value was found.

A Discord webhook is a tool that allows you to send messages to a Discord channel from an external source. It is a URL that enables you to send messages to a specific Discord channel from your own website, application, or other platform. The messages appear as if they were sent by a user within Discord, but they are actually sent programmatically. This allows you to integrate Discord into your own systems, such as sending notifications, updates, or other automated messages.


```go 
 package discord 

import (
	"os"
	"log"
	"encoding/json"
	"net/http"
	"github.com/dli-invest/finreddit/pkg/types"
	"bytes"
)

func SendWebhook(discordWebhook types.DiscordPayload) (*http.Response, error){
	discordUrl := os.Getenv("DISCORD_WEBHOOK")
	if discordUrl == "" {
		log.Fatal("DISCORD_WEBHOOK not set")
	}
	webhookData, err := json.Marshal(discordWebhook)
	if err != nil {
		log.Fatal(err)
	}
	resp, err := http.Post(discordUrl, "application/json", bytes.NewBuffer(webhookData))
	return resp, err
}
 
 ```

This is a Go function named "SendWebhook" that posts a Discord webhook to a specified Discord channel. The Discord webhook URL is obtained from an environment variable named "DISCORD\_WEBHOOK". The input to the function is a DiscordPayload of type "types.DiscordPayload" and contains the data to be sent in the webhook. The function then uses the "json" package to marshal the input into a JSON string, and the "http" package to send a HTTP POST request to the Discord webhook URL with the JSON string as the payload. The response from the POST request and any error are returned from the function.


GitHub Actions allows you to automate tasks such as building, testing, and deploying code. It also supports automating tasks to run on a schedule using workflows. You can create a workflow that runs on a schedule using the "schedule" trigger in your workflow file.

Here's an example of a workflow that runs every day at 8pm UTC:


```yaml
name: Schedule Task

on:
 schedule:
 - cron: '0 20 \* \* \*'

jobs:
 task:
 runs-on: ubuntu-latest
 steps:
 - name: Run Task
 run: echo "Running Task on Schedule"
```
This workflow specifies that it should run on a schedule using the `schedule` trigger and the `cron` value of `0 20 * * *`. The `cron` value represents a standard cron syntax that specifies the schedule. In this case, it runs every day at 8pm UTC.

You can add additional steps in the `steps` section to perform any other tasks you need to automate. You can also use environment variables in your workflow to pass in any required information, such as API keys or file paths.


```yaml 
 on:
  schedule:
    # * is a special character in YAML so you have to quote this string
    - cron: '50 * * * *'
  push:
    branches:
      - main

env: 
  REDDIT_CLIENT_ID: ${{ secrets.REDDIT_CLIENT_ID }}
  REDDIT_CLIENT_SECRET: ${{ secrets.REDDIT_CLIENT_SECRET }}
  REDDIT_PASSWORD: ${{ secrets.REDDIT_PASSWORD }}
  REDDIT_USERNAME: ${{ secrets.REDDIT_USERNAME }}
  DISCORD_WEBHOOK: ${{ secrets.DISCORD_REDDIT_WEBHOOK}}

name: Send Updates
jobs:
  run:
    strategy:
      matrix:
        go-version: [1.15.x]
        platform: [ubuntu-latest]
    runs-on: ${{ matrix.platform }}
    steps:
    - name: Install Go
      if: success()
      uses: actions/setup-go@v2
      with:
        go-version: ${{ matrix.go-version }}
    - name: Checkout code
      uses: actions/checkout@v2
    - name: Run job
      run: go run cmd/scan_sr/manga.go

    - name: Commit files
      id: commit
      run: |
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action"
        git add internal/*.csv
        git commit -m "Updating csv"
      continue-on-error: true

    - name: Push changes
      uses: ad-m/github-push-action@master
      continue-on-error: true
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        branch: ${{ github.ref }}
 
 ```

This code is a GitHub Actions workflow that automates the task of sending updates. The schedule of the task is set to run every hour at 50 minutes past the hour, and it will only run when the main branch is pushed.

The workflow sets environment variables for Reddit API credentials (client ID, client secret, password, and username) and a Discord webhook URL, all of which are stored as GitHub secrets.

The job runs on an Ubuntu latest machine and uses Go version 1.15.x. The job checks out the code, runs the scan\_sr/manga.go script, and if successful, commits the updated csv files to the repository and pushes the changes. The action uses a GitHub push action to push the changes.


### References 

* https://github.com/dli-invest/finreddit 
* https://pkg.go.dev/github.com/dli-invest/finreddit
