#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <msg.h>
#include "utils.h"
#include "proto/msg-header.pb-c.h"



int main(int argc, char *args[]) {

    char *filepath = "/tmp/output.bin";
    int size = 0;
    size_t mh_size=0;
    char *content = read_binary(filepath, &size);
    uint8_t *serial = get_message_header(content, size, &mh_size);
    checkNull(serial);
    MessageHeader *mh = message_header__unpack(NULL,mh_size, serial);
    checkNull(mh);
    printf("VIN     : %s\n", mh->vin);
    printf("V       : %d\n", mh->payloadver);
    printf("ARXML   : %d\n", mh->arxmlver);
    printf("SEQ     : %d\n", mh->seq);
    printf("VLAN    : %d\n", mh->vlan);
    printf("TIME    : %llu\n", mh->ts);

    if (content != NULL) free(content);
    message_header__free_unpacked(mh, NULL);

    return 0;
}
