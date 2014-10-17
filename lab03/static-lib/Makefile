all: simple_math

simple_math: simple_math.o
	gcc -Wall simple_math.o -o simple_math

simple_math.o: simple_math.c
	gcc -Wall -c simple_math.c

run: simple_math
	./simple_math

.PHONY: clean
clean:
	rm -f *.o *~ simple_math
