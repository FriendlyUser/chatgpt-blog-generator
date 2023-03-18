rewrite the outline so that the book outline is in yaml and under the sections key for each chapter rewrite with - src: "raw" type: "# Chapter 1: Introduction to Golang" and each subsection is - What is Golang? Example yaml would be: ```yaml sections: - type: "raw" src: "# Chapter 1: Introduction to Golang" - What is Golang? ```


pandoc -f markdown -t html --standalone --toc --toc-depth=3 --css=output/tex/styles.css output/books/unpublished/algos/algorithms_in_golang.md output/books/unpublished/algos/excerises.md -o output_file.html