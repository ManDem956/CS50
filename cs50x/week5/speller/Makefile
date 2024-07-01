ifeq ($(OS),Windows_NT)
  ifeq ($(shell uname -s),) # not in a bash-like shell
	CLEANUP = del /F /Q
	MKDIR = mkdir
  else # in a bash-like shell, like msys
	CLEANUP = rm -rf
	MKDIR = mkdir -p
  endif
	TARGET_EXTENSION=exe
else
	CLEANUP = rm -rf
	MKDIR = mkdir -p
	TARGET_EXTENSION=out
endif

CD = cd

# .SECONDARY:

CHECK50 = check50 cs50/problems/2024/x/
STYLE50 = style50

.PHONY: clean
.PHONY: test
.PHONY: %
.PHONY: run

PATHU = unity/src/
PATHS = src/
PATHT = test/
PATHB = build/
PATHD = build/depends/
PATHO = build/objs/
PATHR = build/results/

BUILD_PATHS = $(PATHB) $(PATHD) $(PATHO) $(PATHR)

SRCT = $(wildcard $(PATHT)*.c)
SRCS = $(wildcard $(PATHS)*.c)

undefine CFLAGS

COMPILE=clang -c -g
LINK=clang
DEPEND=gcc -MM -MG -MF 
CFLAGS=-I. -I$(PATHU) -I$(PATHS) -ggdb3 -gdwarf-4 -O0 -Qunused-arguments -std=c11 -Wall -Werror -Wextra -Wno-gnu-folding-constant -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow

# COMPILE=clang
# LINK=clang -v
# DEPEND=clang -MM -MG -MF 
# CFLAGS=-ferror-limit=1 -gdwarf-4 -ggdb3 -O0 -std=c11 -pedantic -Wall -Werror -Wextra -Wno-gnu-folding-constant -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wno-unused-but-set-variable -Wshadow -Wnonportable-include-path -I. -I$(PATHU) -I$(PATHS)

# from CS50
CS50LIBS = -lm

RESULTS = $(patsubst $(PATHT)Test%.c,$(PATHR)Test%.txt,$(SRCT) )
RUNPATHS = $(patsubst $(PATHS)%.c,$(PATHB)%,$(SRCS) )
OBJPATHS = $(patsubst $(PATHS)%.c,$(PATHO)%.o,$(SRCS) )


PASSED = `grep -s PASS $(PATHR)*.txt`
FAIL = `grep -s FAIL $(PATHR)*.txt`
IGNORE = `grep -s IGNORE $(PATHR)*.txt`

run: $(filter $(MAKECMDGOALS:%=$(PATHB)%), $(RUNPATHS))
	./$< $(ARGS)

%: $(PATHB)% #$(PATHD)Test%.d
	@echo Building....

validate/%:
	$(CD) $(PATHS) ; pwd ; $(CHECK50)$(*F); $(STYLE50) $(*F).c

test: CFLAGS += -DTEST
test: $(BUILD_PATHS) $(RESULTS)
	@echo "-----------------------\nIGNORES:\n-----------------------"
	@echo "$(IGNORE)"
	@echo "-----------------------\nFAILURES:\n-----------------------"
	@echo "$(FAIL)"
	@echo "-----------------------\nPASSED:\n-----------------------"
	@echo "$(PASSED)"
	@echo "\nDONE"

$(PATHR)%.txt: $(PATHB)%.$(TARGET_EXTENSION)
	-./$< > $@ 2>&1

$(PATHB)%: $(PATHO)%.o  $(filter-out $(MAKECMDGOALS:%=$(PATHO)%.o), $(OBJPATHS)) #$(PATHD)%.d
	$(LINK)  -o  $@  $^ $(CS50LIBS)

$(PATHB)Test%.$(TARGET_EXTENSION): $(PATHO)Test%.o $(PATHO)dictionary.o $(PATHO)unity.o #$(PATHD)Test%.d
	$(LINK)  -o  $@  $^ $(CS50LIBS)

$(PATHO)%.o:: $(PATHT)%.c
	$(COMPILE) $(CFLAGS) $< -o $@ $(CS50LIBS)

$(PATHO)%.o:: $(PATHS)%.c $(PATHS)%.h
	$(COMPILE) $(CFLAGS) $< -o $@ $(CS50LIBS)

$(PATHO)%.o:: $(PATHU)%.c $(PATHU)%.h	
	$(COMPILE) $(CFLAGS) $< -o $@ $(CS50LIBS)

$(PATHD)%.d:: $(PATHT)%.c
	$(DEPEND) $@ $<

$(PATHB):
	$(MKDIR) $(PATHB)

$(PATHD):
	$(MKDIR) $(PATHD)

$(PATHO):
	$(MKDIR) $(PATHO)

$(PATHR):
	$(MKDIR) $(PATHR)

clean:
	$(CLEANUP) $(PATHB)
	$(MKDIR) $(BUILD_PATHS)

.PRECIOUS: $(PATHB)Test%.$(TARGET_EXTENSION)
.PRECIOUS: $(PATHD)%.d
.PRECIOUS: $(PATHO)%.o
.PRECIOUS: $(PATHR)%.txt
