rm -rf output
mkdir output

for file in src/images/*; do  ./build/filter -r "$file" output/reversed_$(basename -- "$file") ; done
for file in src/images/*; do  ./build/filter -g "$file" output/greyscale_$(basename -- "$file") ; done
for file in src/images/*; do  ./build/filter -b "$file" output/blur_$(basename -- "$file") ; done
for file in src/images/*; do  ./build/filter -e "$file" output/edges_$(basename -- "$file") ; done