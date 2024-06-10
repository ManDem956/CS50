#!/bin/bash

OPTIND=2
datapath=$1
path='times'
outfile="$path/out.csv"


show_help() {
    echo "
        Usage: <executable name> <file name> [-r]        
        -r  Clenup
"
}

while getopts "rhR:" FLAG; do
    case "$FLAG" in
    R) RUNS="$OPTARG" ;;
    r) CLEANUP=1 ;;
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

RUNS="${RUNS:-20}"

shift $((OPTIND - 1))

if [[ "${CLEANUP}" -eq 1 ]]; then
    echo "Cleaning up"
    rm -rf $path
    mkdir $path
fi

echo "$RUNS"

echo "command|Elapsed real (s)|CPU%">> $outfile
for exec in ./sort*; do
    for filename in "$datapath"/*.txt; do
        COMMAND=("$exec" "$filename")

        echo "Runnig '${COMMAND[*]}' $RUNS times..."

        for ((i = 1; i <= RUNS; i++)); do
            /usr/bin/time -o $outfile -a -f "'%C'|%e|%P" "${COMMAND[@]}" >/dev/null 2>&1
        done
    done
done
