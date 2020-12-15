import msgheader
import msg_header_pb2
import json

inputfile='/tmp/output.bin'
with open(inputfile, "rb") as fin:
    data = fin.read()
    # content = msgheader.getMessageHeader(data)
    # mh = msg_header_pb2.MessageHeader()
    # mh.ParseFromString(content)
    # print(mh)
    mh = msgheader.message_header(data)
    print(mh)

