---
tags: ['python', 'introtopython']
title: Chapter 2 Basic syntax and data types.
description: Describing how to use python to program.
pubDate: Fri, 14 June 2024
layout: "@/templates/BasePost.astro"
imgSrc: /imgs/2023/1635327465.png
jupytext:
  formats: md:myst
text_representation:
 extension: .md
 format_name: myst
 format_version: 0.13
 jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
### Basic syntax and data types

Python is a high-level, interpreted programming language that is popular for its simple syntax, readability and ease of use. Understanding the basic syntax of Python is fundamental to writing effective code. In this chapter, we'll discuss Python syntax and data types, including indentation, comments, statements, expressions and operators.

Indentation
Python uses indentation to group statements together. This makes the code more readable and helps to prevent syntax errors. Indentation is typically four spaces, but can be any consistent number of spaces or tabs. It is important to note that mixing tabs and spaces for indentation is not allowed in Python.

Comments
Comments are used to explain the code and are ignored by the Python interpreter. In Python, a single-line comment starts with a hash symbol (#). Multi-line comments can be enclosed in triple quotes ('''). It is good practice to include comments in your code to make it more readable and understandable to others.

Statements
A statement is a unit of code that the interpreter can execute. A statement can be an assignment, a function call, a loop or a conditional statement. In Python, statements are typically separated by a newline character.

Expressions
An expression is a combination of values, variables, operators and function calls that evaluates to a value. Examples of expressions include arithmetic expressions and Boolean expressions. Expressions can be used in statements or as part of other expressions.

Operators
Python has a wide range of operators, including arithmetic operators (+, -, \*, /), comparison operators (==, !=, <, >), logical operators (and, or, not), and bitwise operators (&, |, ~). Operators can be used in expressions to manipulate values and produce new values.

Data Types
Python has several built-in data types, including numbers, strings, lists, tuples and dictionaries. Numbers can be integers or floating-point numbers. Strings are sequences of characters enclosed in single or double quotes. Lists are ordered collections of items that can be of different types. Tuples are similar to lists, but are immutable. Dictionaries are unordered collections of key-value pairs.

Python is a dynamically-typed language, which means that the type of a variable is determined at runtime and can change during the execution of a program. However, Python does provide some tools for type checking:

isinstance() function: This function is used to determine if an object is an instance of a particular class or a subclass thereof. It takes two arguments: the object and the class (or tuple of classes) to check against.
Example:

```python
class MyClass:
    pass

obj = MyClass()
print(isinstance(obj, MyClass))  # Output: True
```

type() function: This function returns the type of an object.

```python
x = 42
print(type(x))  # Output: <class 'int'>
```

Annotations: Python 3 introduced the ability to add type annotations to function parameters and return values. These annotations are not enforced by the Python interpreter, but they can be used by third-party tools to perform static type checking.

```
def greet(name: str) -> str:
    return f"Hello, {name}!"

greet(123)  # This will raise a TypeError at runtime
```

Type hints are a feature in Python that allow you to annotate function and variable definitions with information about the expected types of values. Type hints were introduced in Python 3.5 as an optional feature, but they have become increasingly popular in recent years as a way to help catch errors and make code more maintainable.

Type hints use a syntax similar to variable annotations. For example, to annotate a function that takes two integers and returns their sum, you would use the following syntax:

```python
def add_numbers(a: int, b: int) -> int:
    return a + b
```

Type hints are a feature in Python that allow you to annotate function and variable definitions with information about the expected types of values. Type hints were introduced in Python 3.5 as an optional feature, but they have become increasingly popular in recent years as a way to help catch errors and make code more maintainable.

Type hints use a syntax similar to variable annotations. For example, to annotate a function that takes two integers and returns their sum, you would use the following syntax:

python
Copy code
def add_numbers(a: int, b: int) -> int:
    return a + b
In this example, the a and b parameters are annotated with the int type, indicating that the function expects integer values. The return type of the function is also annotated with int, indicating that the function will return an integer value.

Type hints are not enforced by the Python interpreter, and they do not affect the behavior of your code. However, they can be used by third-party tools and IDEs to provide code completion and catch type-related errors at compile time. The mypy tool is a popular static type checker for Python that can be used to check your code for type errors.

Here are some benefits of using type hints in Python:

Improved code readability: Type hints can make your code easier to understand by making it clear what types of values are expected and returned by functions.
Catch errors earlier: By specifying the types of variables and function parameters, you can catch errors earlier in the development process and reduce the likelihood of runtime errors.
Improve code quality: Type hints can help you write better code by making it easier to reason about and making it more maintainable.
Enhance tooling support: IDEs and other tools can use type hints to provide more accurate code completion and refactoring suggestions.
Overall, type hints are a useful tool for improving the quality and maintainability of your Python code. However, they are not a substitute for good coding practices and thorough testing.


Conclusion
Python syntax is easy to understand and learn. Indentation, comments, statements, expressions and operators are the fundamental components of Python syntax. Understanding these concepts is important for writing effective Python code. In the next chapter, we'll explore variables and data structures in more detail.

### Basic syntax and data types

Python is a high-level, interpreted programming language that provides several built-in data types. These data types are the fundamental building blocks of any Python program. In this chapter, we'll discuss the most commonly used data types in Python, including numbers, strings, booleans, lists, tuples, dictionaries, and sets.

Numbers
In Python, numbers can be represented as integers, floating-point numbers, or complex numbers. Integers are whole numbers, while floating-point numbers have decimal points. Complex numbers have a real and imaginary component.

Strings
Strings are sequences of characters that are enclosed in single or double quotes. They are immutable, which means they cannot be changed after they are created. String manipulation is an essential part of text processing in Python.

Booleans
Boolean values are either True or False. They are used in conditional statements and comparisons to control the flow of a program.

Lists
Lists are ordered collections of items that can be of different types. They are created using square brackets and can be modified by adding, removing, or changing elements.

Tuples
Tuples are similar to lists, but they are immutable, which means they cannot be changed after they are created. They are created using parentheses and can contain elements of different types.

Dictionaries
Dictionaries are unordered collections of key-value pairs. They are created using curly braces and can be used to store and retrieve data based on keys.

Sets
Sets are unordered collections of unique elements. They are created using curly braces and can be used for set operations such as union, intersection, and difference.


In Python, there are a number of reserved words that have special meanings and cannot be used as variable or function names. These reserved words are used by the Python interpreter for specific purposes and are an integral part of the language syntax. Here is a list of all the reserved words in Python:

- False
- None
- True
- and
- as
- assert
- async
- await
- break
- class
- continue
- def
- del
- elif
- else
- except
- finally
- for
- from
- global
- if
- import
- in
- is
- lambda
- nonlocal
- not
- or
- pass
- raise
- return
- try
- while
- with
- yield

These reserved words cannot be used as variable names, function names, or any other identifier in Python code. If you try to use a reserved word as a variable or function name, you will get a syntax error.

It's important to note that some of these reserved words, such as async and await, were only introduced in recent versions of Python and may not be available in older versions. If you are writing code that needs to be compatible with multiple versions of Python, you should be aware of which reserved words are available in each version.

Conclusion
Python provides several built-in data types that can be used to represent different types of data. Numbers, strings, booleans, lists, tuples, dictionaries, and sets are the most commonly used data types in Python. Understanding these data types is essential for writing effective Python code. In the next chapter, we'll explore variables and operators in more detail.

I hope this article has helped you understand the built-in data types in Python. If you have any questions or comments, please feel free to leave them below. Thank you for reading!

Keywords: Python, data types, numbers, strings, booleans, lists, tuples, dictionaries, sets, text processing, conditional statements, comparisons, square brackets, parentheses, curly braces, mutable, immutable, elements, key-value pairs, unique elements, set operations, union, intersection, difference.


### Variables and Operators

In Python, variables are used to store data that can be accessed and manipulated throughout a program. In this chapter, we'll discuss how to create, manipulate and access data using variables, literals, constants and operators.

Variables
Variables are used to store data in memory for later use. In Python, a variable is created by assigning a value to a name using the equals sign (=). For example, `x = 5` creates a variable named `x` and assigns it the value 5. Variables can be used to store numbers, strings, booleans, and other data types.

Literals
Literals are fixed values that are used in Python code. Examples of literals include numbers, strings, and Boolean values. For example, `5` and `"Hello, world!"` are literals.

Constants
Constants are variables whose values do not change throughout a program. In Python, constants are typically defined using uppercase letters. For example, `PI = 3.14159` defines a constant named `PI`.

Operators
Python provides a wide range of operators that can be used to manipulate data. Some of the most commonly used operators include:

* Arithmetic operators: `+`, `-`, `*`, `/`, `%`, `**`
* Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
* Logical operators: `and`, `or`, `not`
* Assignment operators: `=`, `+=`, `-=`, `*=`, `/=`, `%=`
* Bitwise operators: `&`, `|`, `^`, `~`, `<<`, `>>`

Expressions
Expressions are combinations of literals, variables, and operators that evaluate to a value. For example, `x = 5 + 3` is an expression that adds 5 and 3 and assigns the result (8) to the variable `x`.

Accessing Data
Data stored in variables can be accessed and manipulated using expressions and operators. For example, `x = x + 1` increments the value of the variable `x` by 1.

Conclusion
Variables, literals, constants and operators are essential components of Python programming. They allow you to create, manipulate, and access data within your program. Understanding how to use these elements effectively is critical for writing effective Python code. In the next chapter, we'll explore control structures such as loops and conditional statements.

I hope this article has helped you understand how to create, manipulate and access data using variables, literals, constants, and operators in Python. If you have any questions or comments, please feel free to leave them below. Thank you for reading!

Keywords: Python, variables, literals, constants, operators, arithmetic operators, comparison operators, logical operators, assignment operators, bitwise operators, expressions, accessing data, control structures, loops, conditional statements, data manipulation, data access.


### Input and Output Functions

Input and output (I/O) functions are essential in any programming language. In Python, the two basic I/O functions are `print()` and `input()`. In this chapter, we'll discuss how to use these functions to interact with users and display information to the screen.

Printing to the Console
The `print()` function is used to display output on the console. It can be used to print strings, numbers, and other types of data. For example, `print("Hello, world!")` displays the text "Hello, world!" on the console. Multiple values can be printed using commas, like this: `print("The answer is", 42)`. This prints the string "The answer is" followed by the number 42.

Formatting Output
Python provides a range of formatting options for output. The most common method is to use string interpolation with the `%` operator. For example, `print("The answer is %d" % 42)` prints "The answer is 42". The `%d` is a placeholder for an integer value. Other placeholders include `%s` for strings and `%f` for floating-point numbers.

The `format()` method is another option for formatting output. For example, `print("The answer is {}".format(42))` prints "The answer is 42". The `{}` is a placeholder that is replaced with the value provided in the `format()` method.

Reading Input from the User
The `input()` function is used to read input from the user. It displays a message on the console and waits for the user to enter a value. For example, `name = input("What is your name? ")` prompts the user to enter their name and stores the value in the variable `name`.

Converting Input
The `input()` function always returns a string value. If you need to convert the value to a different data type, you can use functions like `int()`, `float()`, and `bool()`. For example, `age = int(input("How old are you? "))` prompts the user to enter their age and converts the input to an integer value.

Conclusion
The `print()` and `input()` functions are the basic building blocks of input and output in Python. With these functions, you can display information to the user and read input from them. By using formatting options and conversion functions, you can manipulate data in a variety of ways.

I hope this article has helped you understand how to use basic input and output functions such as `print()` and `input()` in Python. If you have any questions or comments, please feel free to leave them below. Thank you for reading!

Here is an example of a basic to-do list implemented in Python using basic syntax and data types:


```python
# Create an empty list to store tasks
tasks = []

# Prompt the user for a new task and add it to the list
while True:
 new_task = input("Enter a new task or type 'exit' to quit: ")
 if new_task == "exit":
  break
 else:
  tasks.append(new_task)
  print("Task added.")

# Print the list of tasks
print("To-Do List:")
for i, task in enumerate(tasks):
  print(f"{i+1}. {task}")
```
This program creates an empty list called `tasks` to store the user's to-do items. It then prompts the user to enter a new task using the `input()` function. If the user types "exit", the program breaks out of the loop and ends. Otherwise, the program adds the new task to the `tasks` list using the `append()` method and prints a message confirming that the task was added.

After the user has entered all of their tasks, the program prints out the entire to-do list using a `for` loop and the `enumerate()` function to number each task. The output looks something like this:


```python
Enter a new task or type 'exit' to quit: Buy groceries
Task added.
Enter a new task or type 'exit' to quit: Walk the dog
Task added.
Enter a new task or type 'exit' to quit: Do laundry
Task added.
Enter a new task or type 'exit' to quit: exit
To-Do List:
1. Buy groceries
2. Walk the dog
3. Do laundry
```
This is just a simple example, but with a few modifications, you could expand it into a more complex to-do list application with features like task prioritization, due dates, and reminders.


