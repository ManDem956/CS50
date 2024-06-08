#!/bin/bash

OPTIND=3
project=$2
path=$1/$project
MAIN="""
int main(int argc, char **argv)
{
    return 0;
}

"""

show_help()
{
echo "
        Usage: <project_name> [-t]

        -t  Create tests
        -r  Clenup
"
}

while getopts "trh" FLAG; do
    case "$FLAG" in
        t) TESTS=1;;
        r) CLEANUP=1 ;;
        h) show_help; exit 1;;
        *) show_help; exit 1;;
    esac
done


pwd

shift $((OPTIND-1))
if [[ "${CLEANUP}" -eq 1 ]]; then
    rm -rf $path
fi

mkdir $path && cp Makefile.template "$_"/Makefile 

cd "$path" || { echo "Error xyz"; exit 1; }

echo "$MAIN" >>  "$project".c

if [[ "${TESTS}" -eq 1 ]]; then
    echo "$MAIN" >> test_"$project".c
fi

IFS=,

files=(*.c)

echo "${files[@]}"

sed -i 's/@PROJECT@/'"${project}"'/g' Makefile 
