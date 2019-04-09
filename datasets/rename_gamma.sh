#!/bin/bash
for file in *.png
do
    mv "$file" "${file%.png}_gamma.png"
done
