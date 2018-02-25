# http://blog.csdn.net/my_offer/article/details/7430993
# must compile file.cpp before compling main.cpp
all:
	g++ -c file.cpp -o file.o
	g++ file.o main.cpp -o go

# merge two lines into one line
once:
	g++ file.cpp main.cpp -o go

clean:
	rm *.out go *.o

