CC = gcc
CFLAGS = -g -Wall -O0

.PHONY: all clean

all: main

main: main.o

main.o: main.c

run: main
	time ./main

clean:
	rm -f *.o *~ main
