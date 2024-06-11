#!/bin/bash

OPTIND=3
project=$2
path=$1/$project
h_header="${project^^}_H"

MAIN="
#include <cs50.h>
#include <stdio.h>
#include <string.h>

#ifndef TEST
int main(int argc, char **argv)
{
    return 0;
}
#endif
"
MAIN_TEST="
#include <cs50.h>
#include <stdio.h>
#include <string.h>

#include \"../src/$project.h\"
#include \"../unity/src/unity.h\"

void test_dummy(void)
{
    TEST_ASSERT_EQUAL_STRING(\"FOLLE\", \"FOLLE\"));
}

void setUp(void)
{
}

void tearDown(void)
{
}

int main(int argc, char **argv)
{
    UNITY_BEGIN();
    RUN_TEST(test_dummy);
    UNITY_END();
}
"

HEADER="
#ifndef ${h_header}
#define ${h_header}

#include <cs50.h>
#include <stdio.h>
#include <string.h>

#endif //${h_header}
"

GITIGNORE="
Makefile
"

show_help() {
    echo "
        Usage: <project_name> [-t]

        -t  Create tests
        -r  Clenup
"
}

while getopts "trh" FLAG; do
    case "$FLAG" in
    t) TESTS=1 ;;
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

pwd

shift $((OPTIND - 1))
if [[ "${CLEANUP}" -eq 1 ]]; then
    rm -rf "$path"
fi

mkdir "$path" && cp Makefile "$_"/Makefile

cd "$path" || {
    echo "Error xyz"
    exit 1
}
mkdir src

echo "$MAIN" >>src/"$project".c
echo "$HEADER" >>src/"$project".h
echo "$GITIGNORE" >>.gitignore

if [[ "${TESTS}" -eq 1 ]]; then
    mkdir test
    echo "$MAIN_TEST" >>test/Test"$project".c
fi

ln -s ~/mine/Unity unity
