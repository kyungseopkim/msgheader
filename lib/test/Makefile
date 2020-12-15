
CFLAGS=-I..
LDFLAGS= -lprotobuf-c
CC=cc

.PHONY: clean

test_msg : test_msg.o utils.o ../msgheader.a
	$(CC) $(LDFLAGS) -o $@ $^

test_msg.o : test_msg.c
	$(CC) -c $(CFLAGS) -o $@ $^


clean:
	rm -f *.o tst_msg
