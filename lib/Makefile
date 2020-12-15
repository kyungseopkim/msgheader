
CC=g++
CFLAGS=-g -std=c++11 -stdlib=libc++ -I/usr/local/include
DEPS = msg.h
SRCS = $(wildcard *.cc)
OBJS = $(SRCS:.cc=.o)
#LDLIBS= -llz4 -lprotobuf

.PHONY: clean all

all: libmsgheader.a

libmsgheader.a: $(OBJS)
	$(AR) rcs $@ $^

#%.o: %.cpp $(DEPS)
#	$(CC) -c $(CFLAGS) -o $@ $<

msg-header.pb.o : msg-header.pb.cc msg-header.pb.h
	$(CC) -c $(CFLAGS)  -o $@ $<

msg.o : msg.cc
	$(CC) -c $(CFLAGS)  -o $@ $<

clean:
	rm -rf  *.o *.a
