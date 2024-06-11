#!/bin/bash

OPTIND=2
datapath=$1
outfile="$path/out.csv"

show_help() {
    echo "
        Usage: <executable name> <file name> [-r]
        -r  Clenup
"
}

while getopts "rnhR:o:" FLAG; do
    case "$FLAG" in
    R) RUNS="$OPTARG" ;;
    r) CLEANUP=1 ;;
    n) DEVNULL=1 ;;
    o) path="$OPTARG" ;;
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
path=${path:-times}

shift $((OPTIND - 1))

redirect_cmd() {
    if [ -n "$DEVNULL" ]; then
        "$@" >/dev/null
    else
        "$@"
    fi
}

if [[ "${CLEANUP}" -eq 1 ]]; then
    echo "Cleaning up"
    rm -rf $path
    mkdir $path
fi

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

        COMMAND=("$exec" "$filename")

        echo "Runnig '${COMMAND[*]}' $RUNS times..."

        for ((i = 1; i <= RUNS; i++)); do
            echo -ne "Run ${i}/$RUNS"\\r
            # set -x
            shopt -s extglob
            redirect_cmd /usr/bin/time -o "$outfile" -a -f "${exec##*/}|${outfilename%%+([0-9])}|${outfilename##+([a-z])}|%e|%P|%k|%x" "${COMMAND[@]}"
            shopt -u extglob
            # set +x
        done

        shopt -u extglob
    done
done
