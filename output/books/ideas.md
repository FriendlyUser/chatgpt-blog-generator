
- sql
- asp.net core
- flutter
- dart
- stats with R
- backend development with express in nodejs
- backend development with spring boot in java
- backend development with django in python
- backend development with flask in python
- wordpress in php
- backend with laravel
- backend with rails
- ruby
- swift
- objective c
- technical analysis with python
- backend development in dart
- nosql with mongodb and nodejs
- scala
- C++ and C
- AutoHotKey for automation
- gui development in python
- frontend css with tailwindcss (add one dhiwise components set)

------

  Write a book outline for an Introduction to Angular. 

  Ensure 4 to 7 points per chapter and at least 13 chapters. Ensure one point is for exercises and another is for solution to exercises.

  In the later chapters, write simple projects users can reference.

  Ensure the content is original and does not infridge on copyright.


------


rewrite the outline so that the book outline is in yaml and under the sections key

for each chapter rewrite with

- src: "raw"
  type: "# Introduction to PowerShell"

and each subsection is 

- "Overview of PowerShell?"
Example yaml would be:

```yaml
sections:
- type: "raw"
  src: "# Chapter 1: Introduction to PowerShell"
- "Overview of PowerShell?"
```


------
BOOK PROMPT

Title: Introduction to Angular. For the above title in a technical book use future prompts to write for a technical audience for a book and give concise explanations for code. Ensure the content is original and does not infringe on copyright. Try not to repeat the code in the book. Respond with 'confirm' to acknowledge that you understand the prompt.

------

pandoc -f markdown -t html --standalone --toc --toc-depth=3 --css=output/tex/styles.css output/books/powershell/powershell.md -o output_file.html