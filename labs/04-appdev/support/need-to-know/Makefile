main: main.o a.o b.o
	gcc -o main main.o a.o b.o -lm

a.o: a.c a.h
	gcc -c a.c -o a.o

b.o: b.c b.h
	gcc -c b.c -o b.o

main.o: main.c
	gcc -c main.c -o main.o

clean:
	rm -f *.o main
