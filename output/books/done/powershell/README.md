Title: Introduction to Automation with Powershell. For the above title in a technical book use future prompts to write for a technical audience for a blog post and give consise explainations for code. Ensure the content is original and does not infridge on copyright. Try not to repeat the code in the post. Respond with 'confirm' to acknowledge that you understand the prompt.

--------

Write a book outline for an Introduction to Automation with Powershell. 

Ensure 5 to 6 points per chapter and at least 13 chapters.

In the later chapters, write simple projects users can use to automate their work.

Ensure the content is original and does not infridge on copyright.

--------

rewrite the outline so that the book outline is in yaml and under the sections key

for each chapter rewrite with

- src: "raw"
  type: "# Introduction to PowerShell"

and each subsection is 

- What is Kotlin and why use it?
Example yaml would be:

```yaml
sections:
- type: "raw"
  src: "# Chapter 1: Introduction to PowerShell"
- Overview of PowerShell?
```


pandoc -f markdown -t html --standalone --toc --toc-depth=3 --css=output/tex/styles.css output/books/powershell/powershell.md -o output_file.html