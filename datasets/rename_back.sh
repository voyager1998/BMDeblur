for file in *.png
do
    mv "$file" "${file/_gamma/}"
done
