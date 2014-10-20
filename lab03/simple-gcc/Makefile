all:
	gcc simple_hello.c -o simple

utils.o: utils.c
	gcc -c utils.c

hello.o: hello.c
	gcc -c hello.c

build: utils.o hello.o
	gcc utils.o hello.o -o hello

clean:
	rm *.o hello
