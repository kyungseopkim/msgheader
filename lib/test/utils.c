//
// Created by Jerry Kim on 12/8/20.
//
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

void checkNull(void *dt) {
    if (dt == NULL) {
        fprintf(stderr, "error pointer null");
        exit(-1);
    }
}

int get_size(FILE *f) {
    fseek(f, 0, SEEK_END);
    int fsize = ftell(f);
    fseek(f, 0, SEEK_SET);
    return fsize;
}

char *read_binary(const char *filepath, int *size) {
    FILE *fp = fopen(filepath, "rb");
    checkNull(fp);
    *size = get_size(fp);

    char *content = (char *) malloc(*size);
    checkNull(content);

    int read_size = fread(content, sizeof(char), *size, fp);
    assert(read_size == *size);
    fclose(fp);

    return content;
}