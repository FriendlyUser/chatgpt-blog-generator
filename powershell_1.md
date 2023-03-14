---
tags: ['bash']
title: Automation with Powershell
description: Getting started with powershell
pubDate: Fri, 14 December 2024
layout: "@/templates/BasePost.astro"
imgSrc: /imgs/2023/3614994253.png
---
# Chapter 1: Introduction to PowerShell
PowerShell is a command-line shell and scripting language developed by Microsoft. It is designed to automate administrative tasks and manage configurations in Windows-based systems. PowerShell provides access to various system management features through commands called cmdlets, which can be used to perform various administrative tasks such as managing files and folders, configuring network settings, and managing user accounts. PowerShell is also capable of running scripts, allowing for automation of complex tasks. PowerShell's scripting capabilities, combined with its access to the .NET framework, make it a powerful tool for managing Windows systems.


PowerShell is a command-line shell and scripting language developed by Microsoft for Windows-based systems. It provides an efficient way to manage and automate administrative tasks, allowing system administrators to accomplish more in less time.

PowerShell is built on top of the .NET framework, which provides access to a wide range of system management features. It is designed to be easy to use, with a simple and consistent syntax that is easy to learn.

PowerShell commands are called cmdlets, which are used to perform specific tasks. Cmdlets can be combined to create complex scripts, allowing for the automation of repetitive tasks. PowerShell scripts can also be used to create functions and modules, making it easy to reuse code and simplify administration.

PowerShell is highly customizable, with the ability to create custom modules and extend its capabilities through the use of third-party modules. It is also cross-platform, with PowerShell Core available for Linux and macOS in addition to Windows.

Overall, PowerShell provides a powerful and flexible tool for managing and automating administrative tasks in Windows-based systems.


There are many benefits to using PowerShell for managing and automating administrative tasks in Windows-based systems. Here are a few:

1. Increased productivity: PowerShell can automate repetitive tasks, allowing administrators to accomplish more in less time. This can help to increase overall productivity and reduce the risk of human error.
2. Easy to learn: PowerShell has a simple and consistent syntax, making it easy to learn for those who are familiar with other command-line interfaces.
3. Integration with .NET: PowerShell is built on top of the .NET framework, which provides access to a wide range of system management features. This integration allows for easy access to system resources and makes it easy to extend PowerShell's capabilities.
4. Flexibility: PowerShell is highly customizable, with the ability to create custom modules and extend its capabilities through the use of third-party modules. This flexibility makes it a powerful tool for managing a wide range of systems and environments.
5. Cross-platform support: PowerShell Core is available for Linux and macOS in addition to Windows, making it a versatile tool for managing systems in mixed-OS environments.

Overall, PowerShell provides a powerful and flexible tool for managing and automating administrative tasks in Windows-based systems, with benefits that include increased productivity, ease of use, flexibility, and cross-platform support.


PowerShell has some unique features that set it apart from other scripting languages, such as Bash, Python, and Ruby.

1. Integration with .NET: PowerShell is built on top of the .NET framework, which provides access to a wide range of system management features. This integration allows PowerShell to easily interact with other .NET-based applications and makes it a powerful tool for managing Windows-based systems.
2. Simple syntax: PowerShell has a simple and consistent syntax that is easy to learn for those who are familiar with other command-line interfaces. This can help to reduce the learning curve for new users and make it easier to create and modify scripts.
3. Strong object-oriented programming (OOP) capabilities: PowerShell is an object-oriented scripting language, which means that it is designed to work with objects rather than just text. This makes it easier to work with complex data structures and simplifies many common administrative tasks.
4. Built-in support for remote administration: PowerShell has built-in support for remote administration, which allows administrators to manage systems from a remote location. This can be especially useful for managing large or geographically distributed environments.
5. Cross-platform support: PowerShell Core is available for Linux and macOS in addition to Windows, making it a versatile tool for managing systems in mixed-OS environments.

While other scripting languages like Bash, Python, and Ruby have their own strengths and are widely used in the industry, PowerShell's unique combination of features makes it a powerful and flexible tool for managing and automating administrative tasks in Windows-based systems.


PowerShell is built into Windows operating systems, starting with Windows 7 and Server 2008 R2. To open PowerShell on Windows, follow these steps:

1. Click on the Start menu or press the Windows key.
2. Type "PowerShell" in the search bar.
3. Click on the "Windows PowerShell" or "PowerShell" application that appears.

If you prefer to use the PowerShell Integrated Scripting Environment (ISE), which provides a more advanced editor with additional features, you can follow these steps:

1. Click on the Start menu or press the Windows key.
2. Type "PowerShell ISE" in the search bar.
3. Click on the "Windows PowerShell ISE" application that appears.

If you are using an older version of Windows that does not include PowerShell, you can download it from the Microsoft website. PowerShell Core, which is the cross-platform version of PowerShell, can also be downloaded from the Microsoft website.

To download PowerShell from the Microsoft website, follow these steps:

1. Go to <https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows?view=powershell-7.1>.
2. Click on the download link for the version of PowerShell that you want to install.
3. Follow the prompts to download and install PowerShell.

Once PowerShell is installed on your system, you can open it by following the steps outlined above.


# Chapter 2: PowerShell Basics
In PowerShell, there are three main types of commands: cmdlets, aliases, and functions.

1. Cmdlets: Cmdlets are the primary type of command used in PowerShell. They are small, single-purpose commands that perform a specific action, such as retrieving information or modifying a system setting. Cmdlets follow a specific naming convention, consisting of a verb followed by a noun, such as Get-Process or Set-ItemProperty. Cmdlets can be used on their own or combined with other cmdlets to create more complex scripts.
2. Aliases: Aliases are shortcuts for cmdlets, functions, or scripts. They are useful for reducing the amount of typing required to execute a command. For example, the alias "ls" can be used in place of the cmdlet "Get-ChildItem" to list the contents of a directory. Aliases can also be created for custom functions or scripts.
3. Functions: Functions are blocks of code that perform a specific action. They are similar to cmdlets, but are designed to be more flexible and reusable. Functions can be defined in PowerShell using the "function" keyword, followed by a name and a block of code. Functions can take parameters and return values, making them a powerful tool for automation and scripting.

It's important to note that aliases and functions are not the same as cmdlets. While they can be used to simplify and customize PowerShell commands, they do not have the same level of built-in functionality as cmdlets. Cmdlets are the most powerful and flexible type of command in PowerShell, and are generally the best choice for performing administrative tasks.


In PowerShell, variables are used to store data for later use in a script or command. Variables can hold a wide range of data types, including strings, integers, arrays, and objects.

To create a variable, use the "$" symbol followed by a name and an equals sign, like this:


```powershell
$myVariable = "Hello, World!"
```
This creates a variable named "myVariable" and assigns it the value "Hello, World!".

PowerShell supports several data types, including:

1. String: A sequence of characters enclosed in single or double quotes.


```powershell
$myString = "This is a string."
```
2. Integer: A whole number without a decimal point.


```powershell
$myInt = 42
```
3. Double: A number with a decimal point.


```powershell
$myDouble = 3.14159
```
4. Boolean: A value that is either "true" or "false".


```powershell
$myBoolean = $true
```
5. Array: An ordered collection of values.


```powershell
$myArray = @("Apple", "Banana", "Cherry")
```
6. Object: A complex data type that can contain multiple properties and methods.


```powershell
$myObject = [PSCustomObject]@{
 Name = "John Smith"
 Age = 35
 Email = "john.smith@example.com"
}
```
To display the value of a variable, simply type its name:


```powershell
$myVariable
```
This will output the value of the variable to the console.

PowerShell also supports type conversion, which allows you to convert a variable from one data type to another. For example, to convert a string to an integer, you can use the "int" function:


```powershell
$myString = "42"
$myInt = [int]$myString
```
This will convert the string "42" to an integer and assign it to the variable "myInt".


In PowerShell, operators are used to perform various operations on variables and data types. There are several types of operators, including arithmetic, comparison, logical, and assignment operators.

Arithmetic operators are used to perform mathematical operations, such as addition, subtraction, multiplication, division, and modulus. The following arithmetic operators are supported in PowerShell:

* Addition: `+`
* Subtraction: `-`
* Multiplication: `*`
* Division: `/`
* Modulus: `%`

For example:


```powershell
$a = 10
$b = 5

$c = $a + $b # Adds 10 and 5, result is 15
$d = $a * $b # Multiplies 10 and 5, result is 50
$e = $a % $b # Computes 10 modulo 5, result is 0
```
Comparison operators are used to compare values and return a Boolean value of `true` or `false`. The following comparison operators are supported in PowerShell:

* Equal to: `eq`
* Not equal to: `ne`
* Greater than: `gt`
* Less than: `lt`
* Greater than or equal to: `ge`
* Less than or equal to: `le`

For example:


```powershell
$a = 10
$b = 5

$c = $a -eq $b # Tests whether 10 is equal to 5, result is false
$d = $a -gt $b # Tests whether 10 is greater than 5, result is true
$e = $a -lt $b # Tests whether 10 is less than 5, result is false
```
Logical operators are used to combine and manipulate Boolean values. The following logical operators are supported in PowerShell:

* And: `-and`
* Or: `-or`
* Not: `-not`

For example:


```powershell
$a = $true
$b = $false

$c = $a -and $b # Tests whether $a and $b are both true, result is false
$d = $a -or $b # Tests whether $a or $b is true, result is true
$e = -not $a # Negates the value of $a, result is false
```
Finally, assignment operators are used to assign values to variables. The following assignment operators are supported in PowerShell:

* Assignment: `=`
* Addition assignment: `+=`
* Subtraction assignment: `-=`
* Multiplication assignment: `*=`
* Division assignment: `/=`
* Modulus assignment: `%=`

For example:


```powershell
$a = 10

$a += 5 # Adds 5 to the value of $a, result is 15
$a -= 3 # Subtracts 3 from the value of $a, result is 12
$a *= 2 # Multiplies the value of $a by 2, result is 24
```
PowerShell expressions can combine operators and operands to form complex statements. For example:


```powershell
$a = 10
$b = 5

if ($a -gt $b -and $a % 2 -eq 0) {
 Write-Host "The value of $a is greater than $b and even."
}
```
This expression tests whether $a is greater than $b and whether $a is even, and if both conditions are true, it outputs a message to the console.


Control flow statements are used to control the flow of execution in PowerShell scripts. They allow you to execute certain code blocks based on conditions or repeat code blocks multiple times.

#### If-else statements

If-else statements are used to execute a block of code if a condition is true and a different block of code if the condition is false. Here is the basic syntax for an if-else statement in PowerShell:


```powershell
if (condition) {
 # Code to execute if the condition is true
}
else {
 # Code to execute if the condition is false
}
```
Here's an example that uses an if-else statement to check whether a number is greater than 10:


```powershell
$num = 15

if ($num -gt 10) {
 Write-Host "$num is greater than 10"
}
else {
 Write-Host "$num is less than or equal to 10"
}
```
#### Loops

Loops are used to execute a block of code multiple times. PowerShell supports several types of loops, including `for`, `foreach`, `while`, and `do-while`.

##### For loops

For loops are used to iterate over a sequence of values a fixed number of times. Here's the basic syntax for a for loop in PowerShell:


```powershell
for ($i = start_value; $i -le end_value; $i++) {
 # Code to execute on each iteration
}
```
Here's an example that uses a for loop to print the numbers from 1 to 5:


```powershell
for ($i = 1; $i -le 5; $i++) {
 Write-Host $i
}
```
##### Foreach loops

Foreach loops are used to iterate over the elements of a collection. Here's the basic syntax for a foreach loop in PowerShell:


```powershell
foreach ($item in collection) {
 # Code to execute on each iteration
}
```
Here's an example that uses a foreach loop to print the elements of an array:


```powershell
$array = 1, 2, 3, 4, 5

foreach ($item in $array) {
 Write-Host $item
}
```
##### While loops

While loops are used to execute a block of code repeatedly while a condition is true. Here's the basic syntax for a while loop in PowerShell:


```powershell
while (condition) {
 # Code to execute on each iteration
}
```
Here's an example that uses a while loop to print the numbers from 1 to 5:


```powershell
$i = 1

while ($i -le 5) {
 Write-Host $i
 $i++
}
```
##### Do-while loops

Do-while loops are used to execute a block of code at least once and then repeatedly while a condition is true. Here's the basic syntax for a do-while loop in PowerShell:


```powershell
do {
 # Code to execute on each iteration
} while (condition)
```
Here's an example that uses a do-while loop to print the numbers from 1 to 5:


```powershell
$i = 1

do {
 Write-Host $i
 $i++
} while ($i -le 5)
```
#### Switch statements

Switch statements are used to execute different blocks of code based on the value of an expression. Here's the basic syntax for a switch statement in PowerShell:


```powershell
switch (expression) {
 value1 { # Code to execute if the expression matches value1 }
 value2 { # Code to execute if the expression matches value2 }
 default { # Code to
```

# Chapter 3: Working with Files and Folders

In this blog post, we will explore how to navigate the file system using PowerShell. PowerShell provides a powerful set of cmdlets for managing the file system, making it easy to navigate directories, create files and folders, and manipulate file content.

To begin, let's open PowerShell by typing "powershell" into the Start menu or by pressing the Windows key + X and selecting "Windows PowerShell."

Once in PowerShell, you can use the "cd" command to change the current directory. For example, if you want to navigate to the "Documents" folder in your user profile, you would type the following command:


```powershell
cd $env:USERPROFILE\Documents
```
This will change the current directory to the "Documents" folder in your user profile. Note that the "$env:USERPROFILE" variable refers to your user profile directory, which is usually located at "C:\Users\username" (where "username" is your username).

To list the contents of the current directory, you can use the "Get-ChildItem" cmdlet:


```powershell
Get-ChildItem
```
This will list all the files and directories in the current directory. By default, the output includes the name, size, and last modified date of each item.

You can also use the "Set-Location" cmdlet to change the current directory:


```powershell
Set-Location C:\Windows\System32
```
This will change the current directory to the "System32" folder in the "C:\Windows" directory.

In addition to navigating the file system, PowerShell provides many other cmdlets for working with files and directories. For example, you can use the "New-Item" cmdlet to create a new file or directory:


```powershell
New-Item -ItemType File -Path "C:\temp\myfile.txt"
```
This will create a new file named "myfile.txt" in the "C:\temp" directory. The "-ItemType" parameter specifies that we want to create a file, rather than a directory.

Overall, PowerShell provides a powerful set of tools for navigating and managing the file system. By mastering these tools, you can become much more efficient and effective in your day-to-day work as a systems administrator or IT professional.


In this blog post, we will explore how to create, delete, copy, and move files and folders using PowerShell. These tasks are essential for managing the file system and can be easily accomplished with PowerShell cmdlets.

Creating Files and Folders

To create a new file or folder, we can use the New-Item cmdlet. For example, to create a new file named "example.txt" in the current directory, we can use the following command:


```powershell
New-Item -ItemType File example.txt
```
To create a new folder named "example" in the current directory, we can use the following command:


```powershell
php`New-Item -ItemType Directory example
```
Deleting Files and Folders

To delete a file or folder, we can use the Remove-Item cmdlet. For example, to delete the file "example.txt" in the current directory, we can use the following command:


```powershell
Remove-Item example.txt
```
To delete the folder "example" in the current directory, we can use the following command:


```powershell
Remove-Item example
```
Note that when deleting a folder, all of its contents will also be deleted.

Copying Files and Folders

To copy a file or folder, we can use the Copy-Item cmdlet. For example, to copy the file "example.txt" from the current directory to the "C:\Temp" directory, we can use the following command:


```powershell
Copy-Item example.txt C:\Temp
```
To copy the folder "example" from the current directory to the "C:\Temp" directory, we can use the following command:


```powershell
Copy-Item example C:\Temp -Recurse
```
Note that we use the "-Recurse" parameter to copy the contents of the folder as well.

Moving Files and Folders

To move a file or folder, we can use the Move-Item cmdlet. For example, to move the file "example.txt" from the current directory to the "C:\Temp" directory, we can use the following command:


```powershell
Move-Item example.txt C:\Temp
```
To move the folder "example" from the current directory to the "C:\Temp" directory, we can use the following command:


```powershell
Move-Item example C:\Temp
```
Note that when moving a folder, all of its contents will also be moved.

In conclusion, PowerShell provides powerful cmdlets for creating, deleting, copying, and moving files and folders. By mastering these tools, you can become much more efficient and effective in your day-to-day work as a systems administrator or IT professional.


