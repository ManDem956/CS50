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

# echo "$RUNS"
# HEADER=0
for exec in ./sort*; do
    for filename in "$datapath"/*.txt; do

        outfilename=${filename##*/}
        outfilename=${outfilename%.txt}
        outfile="$path/out_${exec##*/}.csv"
        if [[ -z "${HEADER}" ]]; then
            HEADER=1
            echo "Writing header"
            echo "Algoritm|Distribution|Size|Elapsed real (s)|CPU%|Mem(KB)|Exit code" >>"$outfile"
        fi
        shopt -s extglob
        COMMAND=("$exec" "$filename")
        echo "Runnig '${COMMAND[*]}' $RUNS times..."
        # echo ${outfilename##+([a-z])}

        for ((i = 1; i <= RUNS; i++)); do
            echo -ne "Run ${i}/$RUNS"\\r
            /usr/bin/time -o "$outfile" -a -f "${exec##*/}|${outfilename%%+([0-9])}|${outfilename##+([a-z])}|%e|%P|%k|%x" "${COMMAND[@]}" >/dev/null 2>&1
            # sleep 10
        done

        shopt -u extglob
    done
done
