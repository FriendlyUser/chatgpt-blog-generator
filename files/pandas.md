---
tags: ['bs4', 'python', 'pandas']
title: Using pandas and bs4 for web scrapping.
description: Explaining how to use pandas and bs4 for web scrapping.
pubDate: Fri, 14 June 2024
layout: "@/templates/BasePost.astro"
imgSrc: /imgs/2023/3353757144.png
---
Pandas is a popular open-source Python library that provides high-performance data manipulation and analysis tools. It is especially useful for working with structured data, such as tables, spreadsheets, and databases.

Pandas can be used for web scraping in several ways. One common approach is to use pandas to read data from HTML tables on web pages. Here's an example code snippet that demonstrates how to use pandas to read data from an HTML table on a web page:


```python
python`import pandas as pd

url = 'https://en.wikipedia.org/wiki/List\_of\_countries\_by\_GDP\_(nominal)'

tables = pd.read_html(url)
df = tables[2]

print(df.head())
```
In this example, we first import the pandas library using the `pd` alias. We then define the URL of the web page containing the table we want to scrape. We use the `pd.read_html()` function to read all the HTML tables on the web page into a list of pandas DataFrame objects. We then select the third table on the page (`tables[2]`) and assign it to a DataFrame object `df`. Finally, we use the `df.head()` method to print the first few rows of the DataFrame.

This is just one example of how pandas can be used for web scraping. Pandas also provides many other tools for data manipulation, cleaning, and analysis that can be useful for working with web data.


To get the source of a website with a table using BeautifulSoup4 (bs4), you can use the `requests` library to send an HTTP request to the web page and then use BeautifulSoup to parse the HTML content of the page. Here's an example code snippet that demonstrates how to do this:


```python
python`import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List\_of\_countries\_by\_GDP\_(nominal)'

# Send an HTTP request to the web page
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table on the page using its CSS class
table = soup.find('table', {'class': 'wikitable sortable'})

# Get the HTML source code of the table
table_html = str(table)

print(table_html)
```
In this example, we first import the `requests` and `BeautifulSoup` modules. We then define the URL of the web page containing the table we want to scrape. We use the `requests.get()` function to send an HTTP request to the web page and obtain its content. We then pass the content to BeautifulSoup using the `'html.parser'` parser.

Next, we use the `soup.find()` method to locate the table on the page using its CSS class (`'wikitable sortable'`). We then convert the table object to a string using the `str()` function and assign it to a variable `table_html`. Finally, we print the HTML source code of the table.

Note that this example assumes that the web page contains only one table with the CSS class `'wikitable sortable'`. If the page contains multiple tables or if the table you're interested in has a different CSS class, you'll need to modify the code accordingly.


To parse a table on a web page using pandas, you can use the `pandas.read_html()` function. This function can automatically extract tables from a given HTML page and return them as pandas DataFrames. Here's an example code snippet that demonstrates how to do this:


```python
python`import pandas as pd

url = 'https://en.wikipedia.org/wiki/List\_of\_countries\_by\_GDP\_(nominal)'

# Use pandas to read the HTML table on the web page
tables = pd.read_html(url)

# Select the table of interest
df = tables[2]

# Print the first few rows of the DataFrame
print(df.head())
```
In this example, we first import the pandas library using the `pd` alias. We then define the URL of the web page containing the table we want to scrape. We use the `pd.read_html()` function to read all the HTML tables on the web page into a list of pandas DataFrame objects. We then select the third table on the page (`tables[2]`) and assign it to a DataFrame object `df`. Finally, we use the `df.head()` method to print the first few rows of the DataFrame.

Note that the `pd.read_html()` function can also take additional parameters, such as `header`, `index_col`, `skiprows`, `na_values`, etc., to customize the behavior of the table extraction process. You can refer to the pandas documentation for more information on how to use these parameters.


To output the DataFrame obtained from parsing a web page's table to a CSV file using pandas, you can use the `pandas.DataFrame.to_csv()` method. Here's an example code snippet that demonstrates how to do this:


```python
python`import pandas as pd

url = 'https://en.wikipedia.org/wiki/List\_of\_countries\_by\_GDP\_(nominal)'

# Use pandas to read the HTML table on the web page
tables = pd.read_html(url)

# Select the table of interest
df = tables[2]

# Write the DataFrame to a CSV file
df.to_csv('countries\_gdp.csv', index=False)

print('Data saved to countries\_gdp.csv')
```
In this example, we first import the pandas library using the `pd` alias. We then define the URL of the web page containing the table we want to scrape. We use the `pd.read_html()` function to read all the HTML tables on the web page into a list of pandas DataFrame objects. We then select the third table on the page (`tables[2]`) and assign it to a DataFrame object `df`.

Next, we use the `df.to_csv()` method to write the DataFrame to a CSV file named `'countries_gdp.csv'`. The `index=False` parameter specifies that we don't want to include the DataFrame's index column in the output file. Finally, we print a message confirming that the data has been saved to the file.

Note that the `to_csv()` method also supports other parameters, such as `sep`, `header`, `columns`, `encoding`, etc., to customize the output format and behavior. You can refer to the pandas documentation for more information on how to use these parameters.


Pandas is a powerful library for data cleaning and manipulation. Here are some advanced topics and techniques in pandas that can help you clean your data:

1. Handling missing data: Pandas provides several functions to handle missing data, such as `isnull()`, `fillna()`, and `dropna()`. `isnull()` returns a boolean mask indicating which values are missing, `fillna()` replaces missing values with a specified value or method, and `dropna()` removes rows or columns with missing values.
2. Handling duplicates: Pandas provides the `duplicated()` and `drop_duplicates()` functions to detect and remove duplicate rows in a DataFrame.
3. Data type conversion: You can use the `astype()` function to convert the data type of one or more columns in a DataFrame. For example, you can convert a column of strings to numeric values, or convert a column of dates to datetime objects.
4. String manipulation: Pandas provides a set of string methods for Series objects, such as `str.lower()`, `str.upper()`, `str.strip()`, and `str.replace()`, to clean and manipulate string data.
5. Reshaping data: Pandas provides functions to reshape data between "long" and "wide" formats, such as `pivot()`, `melt()`, `stack()`, and `unstack()`. These functions can be used to transform data from one format to another, making it easier to work with and visualize.
6. Data aggregation: Pandas provides the `groupby()` function for grouping data based on one or more columns, and applying aggregation functions, such as `sum()`, `mean()`, `max()`, and `min()`, to the grouped data. This can be useful for summarizing and analyzing data.
7. Data merging and joining: Pandas provides functions to merge and join two or more DataFrames based on common columns, such as `merge()`, `join()`, and `concat()`. These functions can be used to combine data from multiple sources into a single DataFrame.

By using these advanced topics and techniques, you can clean and transform your data into a more usable format for analysis and visualization.


