from msg_header_pb2 import MessageHeader

cdef extern from "msg.h":
    char  *get_message_header(const char *data, int size, int *out)

def getMessageHeader(data: bytes) -> bytes:
    cdef int size
    cdef int *outsize=&size
    cdef char *content = get_message_header(data, len(data), outsize)
    return content[:size]

def message_header(data: bytes) -> MessageHeader:
    msg = MessageHeader()
    content = getMessageHeader(data)
    msg.ParseFromString(content)
    return msg