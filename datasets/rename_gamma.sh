#!/bin/bash
for file in *.JPG
do
    mv "$file" "${file%.JPG}_gamma.JPG"
done
