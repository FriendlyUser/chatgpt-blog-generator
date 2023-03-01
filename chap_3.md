---
tags: ['python', 'introtopython']
title: Chapter 3 Control flow and functions.
description: Describing how to use python to program.
pubDate: Fri, 14 September 2024
layout: "@/templates/BasePost.astro"
imgSrc: /imgs/2023/1895495590.png
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
Conditional statements allow you to execute specific pieces of code based on certain conditions. In Python, the most common conditional statement is the `if` statement. The basic syntax for the `if` statement is:


```python
  if condition:
 # execute this code if the condition is True
```
The `condition` can be any expression that evaluates to a Boolean value (i.e., `True` or `False`). If the `condition` is `True`, then the code inside the `if` block is executed. If the `condition` is `False`, then the code inside the `if` block is skipped.

You can also use the `else` statement to execute code when the `condition` is `False`. The basic syntax for the `if-else` statement is:


```python
if condition:
 # execute this code if the condition is True
else:
 # execute this code if the condition is False
```
If the `condition` is `True`, then the code inside the `if` block is executed, and the code inside the `else` block is skipped. If the `condition` is `False`, then the code inside the `if` block is skipped, and the code inside the `else` block is executed.

Sometimes, you may need to check multiple conditions. In that case, you can use the `elif` statement. The basic syntax for the `if-elif-else` statement is:


```python
if condition1:
 # execute this code if condition1 is True
elif condition2:
 # execute this code if condition2 is True
elif condition3:
 # execute this code if condition3 is True
else:
 # execute this code if all conditions are False
```
The `elif` statement allows you to check multiple conditions in a chain. The code inside the first `if` or `elif` block that evaluates to `True` is executed, and the rest of the code is skipped. If none of the conditions are `True`, then the code inside the `else` block is executed.

Here is an example that shows how to use conditional statements in Python:


```python
x = 10

if x > 0:
 print("x is positive")
elif x < 0:
 print("x is negative")
else:
 print("x is zero")
```
In this example, we use an `if-elif-else` statement to check the value of `x`. If `x` is greater than `0`, then we print "x is positive". If `x` is less than `0`, then we print "x is negative". If `x` is equal to `0`, then we print "x is zero".


Looping statements allow you to repeat a block of code multiple times. In Python, there are two types of loops: `for` and `while` loops.

The `for` loop is used to iterate over a sequence (e.g., a list, tuple, string, etc.). The basic syntax for the `for` loop is:


```python
for variable in sequence:
 # execute this code for each item in the sequence
```
The `variable` is a new variable that takes on the value of each item in the `sequence` for each iteration of the loop. The code inside the `for` block is executed once for each item in the sequence.

Here is an example that shows how to use a `for` loop to iterate over a list:


```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
 print(fruit)
```
In this example, we use a `for` loop to iterate over the `fruits` list. For each item in the list, we print the value of the `fruit` variable.

The `while` loop is used to repeat a block of code as long as a condition is `True`. The basic syntax for the `while` loop is:


```python
while condition:
 # execute this code as long as the condition is True
```
The `condition` can be any expression that evaluates to a Boolean value (i.e., `True` or `False`). The code inside the `while` block is executed repeatedly as long as the condition is `True`.

Here is an example that shows how to use a `while` loop to repeat a block of code:


```python
i = 1

while i <= 10:
 print(i)
 i += 1
```
In this example, we use a `while` loop to print the numbers from `1` to `10`. The loop condition (`i <= 10`) is `True` as long as `i` is less than or equal to `10`. Inside the loop, we print the value of `i` and then increment `i` by `1`. The loop repeats until `i` is greater than `10`.

When using loops, it's important to ensure that the condition or sequence you are using will eventually terminate, or else the loop will continue running indefinitely (known as an infinite loop). To avoid infinite loops, you can use a `break` statement to exit the loop prematurely, or a `continue` statement to skip the current iteration of the loop and move on to the next one.


In Python, you can use `break`, `continue`, and `pass` statements to control the flow of loops.

The `break` statement allows you to exit a loop prematurely. When the `break` statement is encountered inside a loop, the loop is immediately exited and the program continues with the code that comes after the loop.

Here is an example that shows how to use the `break` statement to exit a loop:


```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
 if fruit == "banana":
  break
 print(fruit)
```
In this example, we use a `for` loop to iterate over the `fruits` list. Inside the loop, we check if the value of `fruit` is `"banana"`. If it is, we exit the loop using the `break` statement. If it's not, we print the value of `fruit`.

The `continue` statement allows you to skip the current iteration of a loop and move on to the next one. When the `continue` statement is encountered inside a loop, the current iteration of the loop is skipped, and the loop continues with the next iteration.

Here is an example that shows how to use the `continue` statement to skip an iteration of a loop:


```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
 if fruit == "banana":
  continue
 print(fruit)
```
In this example, we use a `for` loop to iterate over the `fruits` list. Inside the loop, we check if the value of `fruit` is `"banana"`. If it is, we skip the current iteration of the loop using the `continue` statement. If it's not, we print the value of `fruit`.

The `pass` statement is used as a placeholder when you need to include an empty block of code. When the `pass` statement is encountered, nothing happens, and the program continues with the next statement.

Here is an example that shows how to use the `pass` statement to include an empty block of code:


```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
 if fruit == "banana":
  pass
 else:
  print(fruit)
```
In this example, we use a `for` loop to iterate over the `fruits` list. Inside the loop, we check if the value of `fruit` is `"banana"`. If it is, we do nothing using the `pass` statement. If it's not, we print the value of `fruit`.

By using `break`, `continue`, and `pass` statements, you can control the flow of loops in Python and make your code more efficient and readable.


In Python, you can define and call functions using the `def` keyword.

Here is an example of how to define a function:


```python
def greet(name):
 print(f"Hello, {name}!")
```
In this example, we define a function called `greet` that takes one parameter called `name`. Inside the function, we print a message that greets the `name` parameter.

Here is an example of how to call the `greet` function:


```python
greet("John")
```
In this example, we call the `greet` function and pass in the value `"John"` as the `name` parameter. The function then prints the message "Hello, John!".

You can also define functions that take multiple parameters:


```python
def add_numbers(x, y):
 return x + y
```
In this example, we define a function called `add_numbers` that takes two parameters called `x` and `y`. Inside the function, we use the `return` keyword to return the sum of `x` and `y`.

Here is an example of how to call the `add_numbers` function:


```python
result = add_numbers(3, 4)
print(result)
```
In this example, we call the `add_numbers` function and pass in the values `3` and `4` as the `x` and `y` parameters. The function then returns the sum of `3` and `4`, which is assigned to the `result` variable. Finally, we print the value of `result`, which is `7`.

By defining and calling functions with parameters, you can create reusable blocks of code that can be called with different input values to produce different output values.


In Python, you can use the `return` statement to send values back from functions.

Here is an example of a function that uses the `return` statement:


```python
def add_numbers(x, y):
 return x + y
```
In this example, we define a function called `add_numbers` that takes two parameters called `x` and `y`. Inside the function, we use the `return` keyword to return the sum of `x` and `y`.

Here is an example of how to call the `add_numbers` function and assign the return value to a variable:


```python
result = add_numbers(3, 4)
print(result)
```
In this example, we call the `add_numbers` function and pass in the values `3` and `4` as the `x` and `y` parameters. The function then returns the sum of `3` and `4`, which is assigned to the `result` variable. Finally, we print the value of `result`, which is `7`.

You can also use the `return` statement to return multiple values from a function. To do this, you can separate the values with commas:


```python
def square_and_cube(x):
 square = x ** 2
 cube = x ** 3
 return square, cube
```
In this example, we define a function called `square_and_cube` that takes one parameter called `x`. Inside the function, we calculate the square and cube of `x`, and then use the `return` statement to send both values back.

Here is an example of how to call the `square_and_cube` function and assign the return values to variables:


```python
python`square, cube = square_and_cube(2)
print(square)
print(cube)
```
In this example, we call the `square_and_cube` function and pass in the value `2` as the `x` parameter. The function then returns the square and cube of `2`, which are assigned to the `square` and `cube` variables. Finally, we print the values of `square` and `cube`, which are `4` and `8` respectively.

By using the `return` statement, you can send values back from functions, which allows you to use the output of a function in other parts of your program.

In Python, you can use the yield function to create generators.

A generator is a type of iterator that can be used to generate a sequence of values on the fly. Generators are useful for working with large datasets or infinite sequences, as they allow you to generate values one at a time, rather than storing all of the values in memory at once.

Here is an example of a generator function that uses the yield function:

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1
```

In this example, we define a generator function called countdown that takes one parameter called n. Inside the function, we use a while loop to generate a sequence of values from n down to 1. Each time through the loop, we use the yield keyword to send the current value back as the next value in the sequence.

Here is an example of how to use the countdown generator:

```python
for i in countdown(5):
    print(i)
```

In this example, we use a for loop to iterate over the values generated by the countdown generator. Each time through the loop, the next value in the sequence is generated by the yield keyword and printed to the console.

The output of this program would be:

```bash
5
4
3
2
1
```

By using the yield function, you can create generators that generate sequences of values on the fly,