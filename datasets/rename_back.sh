for file in *.JPG
do
    mv "$file" "${file/_gamma/}"
done
