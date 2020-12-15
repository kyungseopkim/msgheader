//
// Created by Jerry Kim on 12/8/20.
//
#include <stdio.h>
#include <stdlib.h>

#include <lz4.h>
#include "utils.h"

//    int estimated_size = LZ4_compressBound(size);
//    char *compressed = (char *)malloc(estimated_size);
//    int compressed_size = LZ4_compress_default(content, compressed, size, estimated_size);
//
//    int request_size = size * 10;
//    printf("Request size %d\n", request_size);
//    char *decompressed = (char *) malloc(request_size);
//    checkNull(decompressed);
//
//    int decompressed_size = LZ4_decompress_safe(compressed, decompressed, compressed_size, request_size);
//    if (decompressed_size < 0) {
//        printf("Decompress is not working %d, %d\n", size, decompressed_size);
//        exit(-1);
//    }

//    if (decompressed != NULL) free(decompressed);


int main() {
    const char * filename = "/tmp/sandbox/batt01.67.1607472055133.3205.baby";
    int compressed_size = 0;
    char *compressed = read_binary(filename, &compressed_size);

    int request_size = compressed_size * 10;
    printf("Request size %d\n", request_size);
    char *decompressed = (char *) malloc(request_size);
    checkNull(decompressed);
    int decompressed_size = LZ4_decompress_safe(compressed, decompressed, compressed_size, request_size);
    if (decompressed_size < 0) {
        printf("Decompress is not working %d, %d\n", compressed_size, decompressed_size);
        exit(-1);
    }


    if (compressed != NULL) free(compressed);

    return 0;
}