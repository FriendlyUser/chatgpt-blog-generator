#!/bin/bash

cd /path/to/repository

## Use Git to list all the authors and their line counts

git ls-files | xargs -n1 git blame --line-porcelain | grep "^author " | sort | uniq -c | sort -nr | while read count author; do
    echo "$author: $count"
done