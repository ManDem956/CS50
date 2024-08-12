#!/bin/bash

extensions=(".doc" ".docx" ".pdf" ".txt" ".rtf" ".odt")
extensions+=(".jpg" ".jpeg" ".png" ".gif" ".bmp" ".tif" ".tiff")
extensions+=(".mp3" ".wav" ".aac" ".flac" ".wma")
extensions+=(".mp4" ".avi" ".mov" ".wmv" ".flv")
extensions+=(".zip" ".rar" ".7z" ".tar" ".gz")
extensions+=(".py" ".js" ".html" ".css" ".java")

OPTIND=1

show_help() {
    echo "
        Usage: create <path> [-n: FILES_COUNT] [-s: path]

        -n  Specify number of files to generate. gefault = 10        
        -s  Specify path to place generated files to, default = 'source/'        
"
}

while getopts "hn:s:" FLAG; do
    case "$FLAG" in
    n) FILES_COUNT=$OPTARG ;;
    s) path=$OPTARG ;;
    h)
        show_help
        exit 1
        ;;
    *)
        show_help
        exit 1
        ;;
    esac
done

shift $((OPTIND - 1))

path=${path:-source}
FILES_COUNT=${FILES_COUNT:-10}
FILES_COUNT=$((FILES_COUNT-1))
echo "Removing $path/"
rm -rf $path

echo "Creating $path/"
mkdir $path

echo ${#FILES_COUNT} 
echo $FILES_COUNT

echo "Creating $FILES_COUNT files for each extension in $path/"
for ext in "${extensions[@]}"
do    
    eval touch $path/test_{$(printf "%0${#FILES_COUNT}d..%0${#FILES_COUNT}d" 0 $((FILES_COUNT)))}$ext
    # eval touch $path/test_{0..$((FILES_COUNT-1))}$ext
    # touch $path/test_${0..$FILES_COUNT}$ext
done
