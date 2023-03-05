---
tags: ['go']
title:  Object-Oriented Programming in Go.
description:  Object-Oriented Programming in Go.
pubDate: Fri, 21 October 2024
layout: "@/templates/BasePost.astro"
imgSrc: /imgs/2023/1452718796.png
---
Object-oriented programming (OOP) is a popular programming paradigm that emphasizes the use of objects, which are instances of classes, to model real-world entities. OOP is widely used in software development because it offers several benefits, such as encapsulation, inheritance, and polymorphism. In this blog post, we'll explore how to implement OOP concepts in Go.

Classes and Objects in Go

Go doesn't have classes like other object-oriented languages such as Java or Python. However, Go does have user-defined types, which can be used to achieve the same functionality as classes. A user-defined type is created using the `type` keyword, followed by the name of the type and the underlying type. For example, we can define a `Person` type as follows:


```go
type Person struct {
 name string
 age int
}
```
In Go, we can create objects using struct literals, which are similar to object literals in JavaScript. Here's an example of creating a `Person` object:


```go
person := Person{name: "John Doe", age: 30}
```
Encapsulation in Go

Encapsulation is the idea of hiding the implementation details of an object from the outside world. In Go, we can achieve encapsulation by using a combination of struct fields and methods. Struct fields that are capitalized are exported and can be accessed from outside the package, while unexported fields can only be accessed from within the package.

Here's an example of encapsulation in Go:


```go
type BankAccount struct {
 owner string
 balance float64
 isLocked bool
}

func (b \*BankAccount) Deposit(amount float64) {
 if !b.isLocked {
 b.balance += amount
 }
}

func (b \*BankAccount) Withdraw(amount float64) {
 if !b.isLocked && b.balance >= amount {
 b.balance -= amount
 }
}

func (b \*BankAccount) Lock() {
 b.isLocked = true
}

func (b \*BankAccount) Unlock() {
 b.isLocked = false
}
```
In this example, we have a `BankAccount` struct that has three fields: `owner`, `balance`, and `isLocked`. We also have four methods: `Deposit()`, `Withdraw()`, `Lock()`, and `Unlock()`. The `Deposit()` and `Withdraw()` methods modify the `balance` field, but only if the account is not locked. The `Lock()` and `Unlock()` methods modify the `isLocked` field.

Inheritance in Go

Inheritance is the idea of creating a new class that is a modified version of an existing class. In Go, we can achieve inheritance by embedding one struct into another.

Here's an example of inheritance in Go:


```go
type Animal struct {
 name string
}

func (a \*Animal) Speak() {
 fmt.Println("My name is", a.name)
}

type Dog struct {
 Animal
 breed string
}

func main() {
 d := Dog{Animal{"Fido"}, "Labrador"}
 d.Speak() // Output: My name is Fido
}
```
In this example, we have an `Animal` struct with a `name` field and a `Speak()` method. We also have a `Dog` struct that embeds the `Animal` struct and has a `breed` field. The `Speak()` method is inherited from the `Animal` struct.

Polymorphism in Go

Polymorphism is the idea of using a single interface to represent multiple types. In Go, we can achieve polymorphism by defining an interface that specifies a set of methods, and then implementing that interface for multiple types.

Here's an example of


A struct is a composite data type that groups together zero or more values with different types under a single name. Structs are similar to classes in object-oriented programming and are commonly used to represent real-world entities. In Go, a struct is defined using the `type` keyword followed by the name of the struct and a set of fields enclosed in curly braces. Here's an example:


```go
type Person struct {
 name string
 age int
}
```
In this example, we define a struct called `Person` with two fields: `name` of type string and `age` of type int.

We can create an instance of the `Person` struct using a struct literal. Here's an example:


```go
p := Person{name: "John", age: 30}
```
This creates a new `Person` object with the `name` field set to "John" and the `age` field set to 30.

We can access the fields of a struct using the dot notation. Here's an example:


```go
sfmt.Println(p.name) // Output: John
fmt.Println(p.age) // Output: 30
```
In Go, all struct fields are public by default, which means they can be accessed from outside the package. If we want to make a field private, we can use a lowercase first letter for the field name. For example:


```go
type Person struct {
 name string
 age int
 email string // private field
}
```
In this example, the `email` field is private and can only be accessed from within the `Person` struct.


In Go, methods are functions that belong to a struct or a type. Methods can be used to encapsulate behavior within a struct, making it easier to work with and maintain. Here's an example of a method in Go:


```go
type Person struct {
 name string
 age int
}

func (p Person) SayHello() {
 fmt.Println("Hello, my name is", p.name)
}
```
In this example, we define a method called `SayHello()` on the `Person` struct. The method takes no parameters and simply prints a greeting to the console.

We can call the `SayHello()` method on an instance of the `Person` struct using the dot notation. Here's an example:


```go
p := Person{name: "John", age: 30}
p.SayHello() // Output: Hello, my name is John
```
Interfaces in Go are similar to interfaces in other programming languages. An interface is a set of method signatures that a type can implement. If a type implements all the methods in an interface, it is said to satisfy the interface. Here's an example of an interface in Go:


```go
type Shape interface {
 Area() float64
}

type Rectangle struct {
 width float64
 height float64
}

func (r Rectangle) Area() float64 {
 return r.width * r.height
}
```
In this example, we define an interface called `Shape` with a single method signature `Area() float64`. We also define a struct called `Rectangle` with two fields `width` and `height`, and a method `Area()` that calculates the area of the rectangle.

We can create an instance of the `Rectangle` struct and use it to satisfy the `Shape` interface. Here's an example:


```go
r := Rectangle{width: 10, height: 5}
var s Shape = r

fmt.Println(s.Area()) // Output: 50
```
In this example, we create a new `Rectangle` object with a width of 10 and a height of 5. We then assign the `Rectangle` object to a variable of type `Shape`. Because the `Rectangle` struct implements the `Area()` method defined in the `Shape` interface, it satisfies the interface and we can call the `Area()` method on the `Shape` variable.


## Todo app with objects

First, you'll want to define your data model using structs. For example, if you're building a CLI app that manages tasks, you might define a Task struct like this:

```go
type Task struct {
    ID        int
    Title     string
    Completed bool
}
```

This struct has three fields: ID, Title, and Completed. You might also define methods on this struct to handle operations like marking a task as completed or updating its title.

Next, you'll want to define your CLI interface using a library like flag or cobra. For example, you might define a task command that has subcommands like list, add, complete, and delete.

To handle these subcommands, you might define a TaskManager struct that has methods like ListTasks(), AddTask(title string), CompleteTask(id int), and DeleteTask(id int). You would then create an instance of this struct in your CLI command handlers and call its methods as needed.

Here's an example of what the task command handler might look like using the cobra library:

```go
func taskCommand() *cobra.Command {
    cmd := &cobra.Command{
        Use:   "task",
        Short: "Manage tasks",
    }

    cmd.AddCommand(taskListCommand())
    cmd.AddCommand(taskAddCommand())
    cmd.AddCommand(taskCompleteCommand())
    cmd.AddCommand(taskDeleteCommand())

    return cmd
}

func taskListCommand() *cobra.Command {
    return &cobra.Command{
        Use:   "list",
        Short: "List all tasks",
        Run: func(cmd *cobra.Command, args []string) {
            manager := NewTaskManager()
            tasks := manager.ListTasks()
            for _, task := range tasks {
                fmt.Printf("%d. [%s] %s\n", task.ID, boolToString(task.Completed), task.Title)
            }
        },
    }
}

func taskAddCommand() *cobra.Command {
    return &cobra.Command{
        Use:   "add",
        Short: "Add a new task",
        Args:  cobra.ExactArgs(1),
        Run: func(cmd *cobra.Command, args []string) {
            manager := NewTaskManager()
            title := args[0]
            manager.AddTask(title)
            fmt.Println("Task added successfully.")
        },
    }
}

func taskCompleteCommand() *cobra.Command {
    return &cobra.Command{
        Use:   "complete",
        Short: "Mark a task as completed",
        Args:  cobra.ExactArgs(1),
        Run: func(cmd *cobra.Command, args []string) {
            manager := NewTaskManager()
            id, err := strconv.Atoi(args[0])
            if err != nil {
                fmt.Println("Invalid task ID.")
                return
            }
            if err := manager.CompleteTask(id); err != nil {
                fmt.Println("Error marking task as completed:", err)
                return
            }
            fmt.Println("Task marked as completed.")
        },
    }
}
```

```go
func taskDeleteCommand() *cobra.Command {
    return &cobra.Command{
        Use:   "delete",
        Short: "Delete a task",
        Args:  cobra.ExactArgs(1),
        Run: func(cmd *cobra.Command, args []string) {
            manager := NewTaskManager()
            id, err := strconv.Atoi(args[0])
            if err != nil {
                fmt.Println("Invalid task ID.")
                return
            }
            if err := manager.DeleteTask(id); err != nil {
                fmt.Println("Error deleting task:", err)
                return
            }
        fmt.Println("Task deleted successfully.")
        },
    }
}
```


In this code, `NewTaskManager()` is a function that returns an instance of the `TaskManager` struct, which is defined elsewhere in your code.

Finally, you'll want to put everything together in your `main()` function. Here's an example of what that might look like:

```go
func main() {
    rootCmd := &cobra.Command{Use: "app"}
    rootCmd.AddCommand(taskCommand())
    if err := rootCmd.Execute(); err != nil {
        fmt.Println(err)
        os.Exit(1)
    }
}
```


This sets up a root command with a subcommand for managing tasks, and then executes the root command using `cobra`. If any errors occur, they'll be printed to the console and the program will exit with a non-zero status code.

That's a very basic overview of how to build a CLI app with object-oriented programming in Go. There are many other details to consider, like error handling, testing, and so on, but hopefully this gives you a starting point to build on.
