CC = g++
CFLAGS = -Wall -g -o

all: consumer generator dispatcher

generator: generator.cpp
	${CC} ${CFLAGS} generator generator.cpp

consumer: consumer.cpp
	${CC} ${CFLAGS} consumer consumer.cpp

dispatcher: dispatcher.cpp
	${CC} ${CFLAGS} dispatcher dispatcher.cpp

clean:
	rm generator consumer dispatcher
