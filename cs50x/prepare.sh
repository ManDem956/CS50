#!/bin/bash

OPTIND=3
project=$2

show_help() {
    echo "
        Usage: <project_name> [-t]

        -t  Create tests
        -r  Clenup
"
}

while getopts "trhd:" FLAG; do
    case "$FLAG" in
    t) TESTS=1 ;;
    r) CLEANUP=1 ;;
    d) project_dir=$OPTARG ;;
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

pwd
project_dir=${project_dir:-$project}
path=$1/$project_dir

shift $((OPTIND - 1))
if [[ "${CLEANUP}" -eq 1 ]]; then
    rm -rf "$path"
fi

mkdir "$path" && cp Makefile.template "$_"/Makefile

# code --add "$path"

cp -rfn .template/src "$path"/src
for f in "$path"/src/*; do mv "$f" "${f/template/$project}"; done
sed -i -e "s/template/$project/g" "$path"/src/*
sed -i -e "s/TEMPLATE/${project^^}/g" "${path}"/src/*

if [[ "${TESTS}" -eq 1 ]]; then
    cp -rn .template/test "$path"/test
    for f in "$path"/test/*; do mv "$f" "${f/template/$project}"; done
    sed -i -e "s/template/$project/g" "$path"/test/*
    sed -i -e "s/TEMPLATE/${project^^}/g" "${path}"/test/*
    ln -s ~/mine/lib/unity "$path"/unity
fi
