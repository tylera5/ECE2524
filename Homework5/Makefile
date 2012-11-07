CC=g++
CFLAGS=-Wall -g -o
SOURCES= driver.cpp exprtest.cpp
EXECUTABLE= exprtest

all: $(EXECUTABLE)

exprtest: 
	bison parser.ypp
	flex -t scanner.ll > scanner.cpp
	${CC} ${CFLAGS} ${EXECUTABLE} ${SOURCES} parser.tab.cpp scanner.cpp 

clean: 
	rm *hh *tab* scanner.cpp exprtest
