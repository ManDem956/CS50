CC= clang
CFLAGS = -ferror-limit=1 -gdwarf-4 -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-gnu-folding-constant -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wno-unused-but-set-variable -Wshadow
LDLIBS = -lcrypt -lcs50 -lm

CS50EXE = check50
CS50PATH = cs50/problems/2024/x

EXE = scrabble

SRCS = scrabble.c
OBJS = $(SRCS:.c=.o)
CS50 = $(CS50PATH)/$(EXE)


$(EXE): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $(OBJS) $(LDLIBS)

verify:
	$(CS50EXE) $(CS50)
	style50 $(SRCS)

say_hello:
	echo "Hello World"