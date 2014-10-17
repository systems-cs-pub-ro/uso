CC = gcc
CFLAGS = -g -Wall -O0

all: main

main: main.o

main.o: main.c

run: main
	time ./main

.PHONY: clean
clean:
	rm -f *.o *~ main
