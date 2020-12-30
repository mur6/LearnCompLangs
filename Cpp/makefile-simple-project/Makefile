CFLAGS = -O0 -g -Wall -std=c++17
SOURCE = test.cpp
PROGRAM = a.out

build: $(PROGRAM)

$(PROGRAM): $(SOURCE)
	clang++ $(CFLAGS) $(SOURCE)

clean:
	rm -f *.o *~ $(PROGRAM)

run: build
	./a.out