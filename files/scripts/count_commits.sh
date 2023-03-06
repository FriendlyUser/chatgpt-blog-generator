#!/bin/bash

## Change to the directory of the Git repository

cd /path/to/repository

## Use Git to list all the authors and their commit counts

git shortlog -s -n --all | while read count author; do
    echo "$author: $count"
done