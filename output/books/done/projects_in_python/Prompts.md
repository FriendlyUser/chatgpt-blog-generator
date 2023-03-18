Write a book outline named Introduction to Python by building projects including

* url shortener
* Create a code generator. This can that take text as input, replaces each letter with another letter, and outputs the “encoded” message.
* Build a counter app. Take your first steps into the world of UI by building a very simple app that counts up by one each time a user clicks a button.
* Build a clock website. How close can you get it to real-time? Can you implement different time zone selectors, and add in the “countdown calculator” functionality to calculate lengths of time?

Ensure 5 to 6 points per chapter and at least 13 chapters.

In the later chapters, write simple projects users can use to automate their work.


-------

Ensure the content is original and does not infridge on copyright.

rewrite the outline so that the book outline is in yaml and under the sections key

for each chapter rewrite with

- src: "raw"
  type: "# Chapter 1: Introduction to Python"

and each subsection is 

- What is Python and why it's a popular language?

Example yaml would be:

```yaml
sections:
- type: "raw"
  src: "# Chapter 1: Introduction to Python"
- What is Python and why it's a popular language?
```