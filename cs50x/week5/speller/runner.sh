rm -rf output
mkdir output
mkdir output/diff

for dict in src/dictionaries/*; 
do  
for text in src/texts/*; 
do
# echo $dict $text
outfile="$(basename -- $dict)_$(basename -- $text)"
./build/speller "$dict" "$text" >> output/"$outfile"_mine.txt ; 
./src/speller50 "$dict" "$text" >> output/"$outfile"_cs50.txt ; 
diff output/"$outfile"_mine.txt output/"$outfile"_cs50.txt >> output/diff/"$outfile"_diff.txt
done;
done
