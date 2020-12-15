#include <iostream>
#include <arpa/inet.h>
#include "msg-header.pb.h"

char *get_message_header(const char *data, int size, int *out) {
    lucid::msg::MessageHeader mh;

    char *cp = (char*) data;
    char *vin = NULL;

    int len = (int)*cp;
    cp += 1;
    vin = (char*)malloc(len+1);
    if (vin == NULL) {
        std::cerr << "Memory Allocation Error" << std::endl;
        return NULL;
    }
    memcpy(vin, cp, len);
    vin[len]=0;
    mh.set_vin(vin);
    cp += len;
    mh.set_payloadver((uint8_t)*cp);
    cp += 1;
    uint32_t arxml = 0;
    memcpy(&arxml, cp, sizeof(uint32_t));
    mh.set_arxmlver(ntohl(arxml));
    cp += sizeof(uint32_t);
    uint16_t seq = 0;
    switch (mh.payloadver()) {
        case 2:
            mh.set_seq((uint8_t)*cp);
            cp += 1;
            mh.set_vlan((uint8_t)*cp);
            cp += 1;
            break;
        case 3:
        case 4:
            memcpy(&seq, cp, sizeof(uint16_t));
            mh.set_seq(ntohs(seq));
            cp += sizeof(short);
            mh.set_vlan(0);
    }

    uint64_t sec = 0;
    memcpy(&sec, cp, sizeof(uint64_t));
    uint64_t epoch = ntohll(sec);
    cp += sizeof(uint64_t);

    uint32_t usec = ntohl((uint32_t)*(uint32_t *)cp);
    cp += sizeof(uint32_t);
    mh.set_ts(epoch * 1000000 + usec);
    *out = mh.ByteSizeLong();
    char *output = (char*)malloc(*out + 1);
    mh.SerializePartialToArray(output, *out);
    free(vin);
    return output;
}
